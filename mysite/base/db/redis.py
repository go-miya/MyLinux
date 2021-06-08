from redis import Redis
import enviroment

redis_client = Redis(host=enviroment.CONFIG['redis_host'], port=enviroment.CONFIG['redis_port'])
