#!/usr/bin/env python3
"""
小宿科技智能搜索 API 客户端
"""

import requests
import json
import sys
import os

def load_config():
    """从 TOOLS.md 或环境变量加载配置"""
    config = {
        'BasePath': os.environ.get('XIAOSU_BASEPATH', ''),
        'Endpoint': os.environ.get('XIAOSU_ENDPOINT', ''),
        'AccessKey': os.environ.get('XIAOSU_ACCESSKEY', '')
    }
    
    # 尝试从 TOOLS.md 读取配置
    tools_path = os.path.expanduser('~/.openclaw/workspace/TOOLS.md')
    if os.path.exists(tools_path):
        with open(tools_path, 'r', encoding='utf-8') as f:
            content = f.read()
            in_section = False
            for line in content.split('\n'):
                if '小宿搜索 API' in line or 'xiaosu' in line.lower():
                    in_section = True
                    continue
                if in_section:
                    if line.startswith('##') or line.startswith('---'):
                        break  # 新章节开始
                    if 'BasePath' in line and ':' in line:
                        config['BasePath'] = line.split(':', 1)[1].strip().strip('`').strip()
                    elif 'Endpoint' in line and ':' in line:
                        config['Endpoint'] = line.split(':', 1)[1].strip().strip('`').strip()
                    elif 'AccessKey' in line and ':' in line:
                        config['AccessKey'] = line.split(':', 1)[1].strip().strip('`').strip()
    
    return config

def search(query, count=10, freshness=None, enableContent=False, 
           contentType='TEXT', mainText=False, sites=None, blockWebsites=None, config=None):
    """执行搜索请求"""
    
    if config is None:
        config = load_config()
    
    if not all([config.get('BasePath'), config.get('Endpoint'), config.get('AccessKey')]):
        return {
            'error': '配置不完整，请在 TOOLS.md 中设置 BasePath, Endpoint, AccessKey',
            'config': config
        }
    
    url = f"https://{config['BasePath']}/search/{config['Endpoint']}/smart"
    
    params = {
        'q': query,
        'count': min(max(count, 1), 50)  # 限制在 1-50 范围内
    }
    
    if freshness:
        params['freshness'] = freshness
    if enableContent:
        params['enableContent'] = 'true'
        params['contentType'] = contentType
        params['mainText'] = 'true' if mainText else 'false'
    if sites:
        params['sites'] = sites
    if blockWebsites:
        params['blockWebsites'] = blockWebsites
    
    headers = {
        'Authorization': f"Bearer {config['AccessKey']}",
        'Pragma': 'no-cache'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': f'请求失败：{str(e)}'}

def format_results(data, count=10):
    """格式化搜索结果"""
    if 'error' in data:
        return f"❌ 错误：{data['error']}"
    
    if not data.get('webPages', {}).get('value'):
        return "未找到相关结果。"
    
    results = data['webPages']['value'][:count]
    output = []
    
    for i, item in enumerate(results, 1):
        title = item.get('name', '无标题')
        url = item.get('url', '')
        snippet = item.get('snippet', '')
        date = item.get('datePublished', '')
        site = item.get('siteName', '')
        score = item.get('score', 0)
        
        output.append(f"{i}. **{title}**")
        output.append(f"   来源：{site} | 相关性：{score:.2f}")
        if date:
            output.append(f"   时间：{date[:10]}")
        output.append(f"   {snippet[:200]}...")
        output.append(f"   🔗 {url}")
        output.append("")
    
    return '\n'.join(output)

def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("用法：python xiaosu_search.py <查询词> [count=10] [freshness=Day|Week|Month] [enableContent=true]")
        sys.exit(1)
    
    query = sys.argv[1]
    kwargs = {}
    
    for arg in sys.argv[2:]:
        if '=' in arg:
            key, value = arg.split('=', 1)
            if key == 'count':
                kwargs['count'] = int(value)
            elif key == 'freshness':
                kwargs['freshness'] = value
            elif key == 'enableContent':
                kwargs['enableContent'] = value.lower() == 'true'
            elif key == 'contentType':
                kwargs['contentType'] = value
            elif key == 'mainText':
                kwargs['mainText'] = value.lower() == 'true'
            elif key == 'sites':
                kwargs['sites'] = value
            elif key == 'blockWebsites':
                kwargs['blockWebsites'] = value
    
    result = search(query, **kwargs)
    print(format_results(result, kwargs.get('count', 10)))

if __name__ == '__main__':
    main()
