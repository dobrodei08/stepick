def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    resp = env['QUERY_STRING'].split("&")
    resp = [item+"\r\n" for item in resp]
    return resp
