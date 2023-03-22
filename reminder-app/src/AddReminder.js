import React, { useState } from 'react';

import React, { useState } from 'react';

function AddReminder(props) {
  const [reminder, setReminder] = useState('');
  const [dateTime, setDateTime] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = {
      reminder: reminder,
      date_time: dateTime
    };

    fetch('/api/reminders', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    }).then(() => {
      props.history.push('/');
    });
  };

  return (
    <div className="container">
      <h1>Add Reminder</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="reminder">Reminder</label>
          <input
            type="text"
            className="form-control"
            id="reminder"
            name="reminder"
            value={reminder}
            onChange={(e) => setReminder(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="dateTime">Date and Time</label>
          <input
            type="datetime-local"
            className="form-control"
            id="dateTime"
            name="dateTime"
            value={dateTime}
            onChange={(e) => setDateTime(e.target.value)}
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Submit
        </button>
      </form>
    </div>
  );
}

export default AddReminder;
