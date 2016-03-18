from django.shortcuts import render
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

# Create your views here.
def index(self, request):
	return render(request, 'index.html', {"title": "Halaman Pack Django 1.9 Socket Server"})

def foobar(self, request):
	redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
	message = RedisMessage('Hello World')
	#and somewhere else
	redis_publisher.publish_message(message)
