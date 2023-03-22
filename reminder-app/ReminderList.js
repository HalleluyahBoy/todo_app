import React, { useState, useEffect } from 'react';

function ReminderList() {
  const [reminders, setReminders] = useState([]);

  useEffect(() => {
    fetch('/api/reminders')
      .then(response => response.json())
      .then(data => setReminders(data));
  }, []);

  return (
    <div className="container">
      <h1>Reminders</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Reminder</th>
            <th>Date and Time</th>
            <th>Edit</th>
            <th>Delete</th>
          </tr>
        </thead>
        <tbody>
          {reminders.map(reminder => (
            <tr key={reminder.id}>
              <td>{reminder.id}</td>
              <td>{reminder.reminder}</td>
              <td>{reminder.date_time}</td>
              <td>
                <a href={'/edit/' + reminder.id}>Edit</a>
              </td>
              <td>
                <form action={'/delete/' + reminder.id} method="post">
                  <button type="submit" className="btn btn-link">
                    Delete
                  </button>
                </form>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="text-center">
        <a href="/add" className="btn btn-primary">
          Add Reminder
        </a>
      </div>
    </div>
  );
}

export default ReminderList;
