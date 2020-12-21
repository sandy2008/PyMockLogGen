from loggen import apache_gen

log_gen = apache_gen(out_path='./apache.log', mode='uniform', rotation=True)
log_gen.run()