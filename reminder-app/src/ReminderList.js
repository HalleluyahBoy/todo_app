import React from 'react';

function ReminderList({ reminders, deleteReminder }) {
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
          {reminders.map((reminder) => (
            <tr key={reminder.id}>
              <td>{reminder.id}</td>
              <td>{reminder.reminder}</td>
              <td>{reminder.date_time}</td>
              <td>
                <a href={`/edit/${reminder.id}`}>Edit</a>
              </td>
              <td>
                <button
                  type="button"
                  className="btn btn-link"
                  onClick={() => deleteReminder(reminder.id)}
                >
                  Delete
                </button>
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
