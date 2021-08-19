import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
#from azure.servicebus import ServiceBusClient, ServiceBusMessage

pg_user = os.environ["POSTGRES_USER"]
pg_pwd = os.environ["POSTGRES_PW"]
pg_url = os.environ["POSTGRES_URL"]
pg_db = os.environ["POSTGRES_DB"]
senderkey = os.environ["SENDGRID_API_KEY"]
CONNECTION_STR = os.environ["ServiceBusConnectionString"]
QUEUE_NAME = os.environ["QueueName"]
admin_email = os.environ["ADMIN_EMAIL_ADDRESS"]


def main(msg: func.ServiceBusMessage):
    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info(
        'Python ServiceBus queue trigger processed message: %s', notification_id)

    # TODO: Get connection to database
    conn = psycopg2.connect(user=pg_user,
                            password=pg_pwd,
                            database=pg_db)

    cursor = conn.cursor()
    print("PostgreSQL server information")
    print(conn.get_dsn_parameters(), "\n")

    try:
        # db operation

        cursor.execute(
            "SELECT message, subject FROM notification WHERE id = %s;", [notification_id])
        notification = cursor.fetchone()
        print("notification ", notification)
        if cursor.rowcount == 0:
            logging.info("notification not found {}".format(notification_id))
            return

        # TODO: Get attendees email and name
        cursor.execute("SELECT first_name, email FROM attendee;")
        attendees = cursor.fetchall()
        print("notification ", attendees)

        # TODO: Loop through each attendee and send an email with a personalized subject
        for attendee in attendees:
            subject = '{}: {}'.format(attendee[0], notification[1])
            send_email(attendee[1], subject, notification[0])

            # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        status = 'Notified {} attendees'.format(len(attendees))
        cursor.execute("UPDATE notification SET status = %s, completed_date = %s WHERE id = %s",
                       (status, datetime.utcnow(), notification_id))
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        # TODO: Close connection
        if conn:
            cursor.close()
            conn.close()


def send_email(email, subject, body):
    message = Mail(
        from_email=admin_email,
        to_emails=email,
        subject=subject,
        plain_text_content=body)

    sg = SendGridAPIClient(senderkey)
    sg.send(message)
