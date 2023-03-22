import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import axios from 'axios';
import ReminderList from './components/ReminderList';
import AddReminder from './components/AddReminder';
import EditReminder from './components/EditReminder';

function App() {
  const [reminders, setReminders] = useState([]);

  useEffect(() => {
    const fetchReminders = async () => {
      const result = await axios('/api/reminders');
      setReminders(result.data);
    };
    fetchReminders();
  }, []);

  const addReminder = async (reminder) => {
    await axios.post('/api/add', reminder);
    setReminders([...reminders, reminder]);
  };

  const editReminder = async (id, updatedReminder) => {
    await axios.post(`/api/edit/${id}`, updatedReminder);
    setReminders(
      reminders.map((reminder) =>
        reminder.id === id ? { ...reminder, ...updatedReminder } : reminder
      )
    );
  };

  const deleteReminder = async (id) => {
    await axios.post(`/api/delete/${id}`);
    setReminders(reminders.filter((reminder) => reminder.id !== id));
  };

  return (
    <Router>
      <Switch>
        <Route path="/" exact>
          <ReminderList reminders={reminders} deleteReminder={deleteReminder} />
        </Route>
        <Route path="/add">
          <AddReminder addReminder={addReminder} />
        </Route>
        <Route path="/edit/:id">
          <EditReminder reminders={reminders} editReminder={editReminder} />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
