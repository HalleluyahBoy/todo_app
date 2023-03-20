import React, { useState } from 'react';
import axios from 'axios';

function ReminderForm() {
  const [user_id, setUserId] = useState('');
  const [reminder, setReminder] = useState('');
  const [date_time, setDateTime] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const reminderData = { user_id, reminder, date_time };
    axios.post('/add_reminder', reminderData)
      .then(response => console.log(response))
      .catch(error => console.log(error));
    setUserId('');
    setReminder('');
    setDateTime('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="user_id">User ID:</label>
      <input type="text" id="user_id" value={user_id} onChange={(event) => setUserId(event.target.value)} /><br />
      <label htmlFor="reminder">Reminder:</label>
      <input type="text" id="reminder" value={reminder} onChange={(event) => setReminder(event.target.value)} /><br />
      <label htmlFor="date_time">Date and Time:</label>
      <input type="datetime-local" id="date_time" value={date_time} onChange={(event) => setDateTime(event.target.value)} /><br />
      <button type="submit">Add Reminder</button>
    </form>
  );
}

export default ReminderForm;
