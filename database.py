from sqlalchemy import create_engine, text

# need to hide this in the future
db_connection_string = "mysql+pymysql://nsxwgri0aylim8kwcvjf:pscale_pw_XNoiyel7ZGcRlv9oqBOEUrpdtkxMaUmJOFCo6c1yvv4@us-east.connect.psdb.cloud/careers?charset=utf8mb4"

engine = create_engine(
	db_connection_string,
	connect_args={
		"ssl": {
			"ssl_ca": "/etc/ssl/cert.pem"
		}
	}
)