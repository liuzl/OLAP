DB_DIR=$HOME/.clickhouse_database
mkdir $DB_DIR
docker run -d --name zliu-clickhouse-server --ulimit nofile=262144:262144 --volume=$DB_DIR:/var/lib/clickhouse yandex/clickhouse-server
