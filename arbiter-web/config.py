arbiter_prod_config = \
    dict(redis_host='10.104.102.142',
         redis_port=6379,
         redis_dj_db=12,
         redis_arbiter_db=9,
         redis_elk_db=11,
         pgsql_host='10.104.104.39',
         pgsql_port='5432',
         pgsql_dbname='arbiter_dj',
         pgsql_user='luna',
         pgsql_password='luna',
         elk_url='10.104.104.57:9200',
         case_path='caseobj/casex')

arbiter_docker_config = \
    dict(redis_host='redis',
         redis_port=6379,
         redis_dj_db=3,
         redis_arbiter_db=9,
         redis_elk_db=11,
         pgsql_host='pgdb',
         pgsql_port='5432',
         pgsql_user='luna',
         pgsql_dbname='arbiter_dj',
         pgsql_password='luna',
         elk_url='elk:9200',
         case_path='caseobj/casex')
