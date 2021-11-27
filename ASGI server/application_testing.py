import uvicorn

'''In the command line, run like:

uvicorn application_testing:app

or programmatically as below.

'''


async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })

if __name__=='__main__':
    uvicorn.run('application_testing:app', host='127.0.0.1', port=5000, log_level="info")
