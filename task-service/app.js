const express = require('express');

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 5001;
const tasks = [];

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', service: 'task-service' });
});

app.get('/tasks', (req, res) => {
  res.json(tasks);
});

app.post('/tasks', (req, res) => {
  const { title, user_id } = req.body || {};
  if (!title) {
    return res.status(400).json({ error: 'title is required' });
  }
  const task = { id: tasks.length + 1, title, user_id, done: false };
  tasks.push(task);
  res.status(201).json(task);
});

app.get('/tasks/:id', (req, res) => {
  const task = tasks.find(t => t.id === Number(req.params.id));
  if (!task) {
    return res.status(404).json({ error: 'not found' });
  }
  res.json(task);
});

app.listen(PORT, () => {
  console.log(`task-service listening on ${PORT}`);
});
