import logging
import faust
import datetime
from faust import Worker

app = faust.App(
    id='hello_world',  # application id
    broker='kafka://127.0.0.1:19092',
    value_serializer='raw',
    store='rocksdb://',
    version=1,
)

greetings_topic = app.topic('greetings')


@app.agent(greetings_topic)
async def consumer(greetings):
    async for greeting in greetings:
        app.logger.info(str(greeting, 'utf-8'))


@app.timer(5)
async def producer():
    now = datetime.datetime.now()
    await greetings_topic.send(value=f'hello, stream {now}, sleep 😴')


if __name__ == '__main__':
    worker = Worker(app=app, loglevel=logging.INFO, debug=True)
    worker.execute_from_commandline()
