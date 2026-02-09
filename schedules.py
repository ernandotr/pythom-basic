import schedule, time;

def job():
    print(time.strftime("%Y-%m-%d %H:%M:%S") + " I'm working...")
# schedule.every(10).seconds.do(job)

schedule.every().day.at("16:00").do(job)
while True:    schedule.run_pending()