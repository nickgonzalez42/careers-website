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

def load_jobs():
	with engine.connect() as conn:
		result = conn.execute(text("select * from jobs"))
		result_all = result.all()
		column_names = result.keys() 
		jobs = []
		for row in result_all:
			jobs.append(dict(zip(column_names, row)))
		return jobs
		
def load_job_from_db(id):
	with engine.connect() as conn:
		result = conn.execute(
			text(f"SELECT * FROM jobs WHERE id = {id}")
		)
		rows = result.all()
		if len(rows) == 0:
			return None;
		else: 
			column_names = result.keys()
			return dict(zip(column_names, rows[0]))