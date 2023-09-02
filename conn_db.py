import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или ":memory:" чтобы сохранить в RAM
cursor = conn.cursor()


# Создание таблицы
cursor.execute(
    "CREATE TABLE Tickets (Ticket_ID INT, Ticket_Date DATE, Person TEXT, Price DECIMAL, Ride_ID INT)")
cursor.execute(
    "CREATE TABLE Rides (Ride_ID INT, Ride_Date DATE, From_City TEXT, To_City TEXT)")


# Вставляем данные в таблицу
cursor.execute(
    "INSERT INTO Tickets (Ticket_ID INT, Ticket_Date DATE, Person TEXT, Price DECIMAL, Ride_ID INT) VALUES ( 1, 'One' ) ")
cursor.execute(
    "INSERT INTO Rides (Ride_ID INT, Ride_Date DATE, From_City TEXT, To_City TEXT) VALUES ( 2, 'Two' ) ")
