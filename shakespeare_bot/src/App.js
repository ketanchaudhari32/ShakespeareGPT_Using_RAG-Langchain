import React, { useState, useEffect } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import CircularProgress from '@mui/material/CircularProgress';

import shakespeareImage from './images/shakespeare.jpg';

function App() {
  const [queryText, setQueryText] = useState('');
  const [responses, setResponses] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleQuerySubmit = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query_text: queryText }),
      });

      const result = await response.json();

      setResponses((prevResponses) => [
        ...prevResponses,
        { query: queryText, response: result.response, sources: result.sources },
      ]);

      setQueryText('');
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const chatHistory = document.getElementById('chat-history');
    if (chatHistory) {
      chatHistory.scrollTop = chatHistory.scrollHeight;
    }
  }, [responses]);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '20px', backgroundColor: '#f4f4f4', minHeight: '100vh', backgroundImage: `url(${shakespeareImage})`, backgroundSize: 'cover', backgroundPosition: 'center', position: 'relative' }}>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', maxWidth: '600px', width: '100%', padding: '20px', backgroundColor: 'rgba(255, 255, 255, 0.8)', borderRadius: '15px', boxShadow: '0 2px 10px rgba(0, 0, 0, 0.1)', position: 'relative' }}>
        <Typography variant="h5" gutterBottom style={{ color: '#333333', marginBottom: '20px' }}>
          William Shakespeare Chat Bot
        </Typography>

        <div id="chat-history" style={{ maxHeight: '400px', overflowY: 'auto', marginBottom: '20px', width: '100%', textAlign: 'left' }}>
          {responses.map((item, index) => (
            <Paper key={index} elevation={3} style={{ padding: '20px', marginBottom: '10px', backgroundColor: '#ffffff', borderRadius: '15px', boxShadow: '0 2px 10px rgba(0, 0, 0, 0.1)' }}>
              <Typography variant="body1" gutterBottom style={{ color: '#333333' }}>
                Query: {item.query}
              </Typography>
              <Typography variant="body1" gutterBottom style={{ color: '#009688' }}>
                Response: {item.response}
              </Typography>
            </Paper>
          ))}
        </div>

        <TextField
          label="Enter your query"
          variant="outlined"
          value={queryText}
          onChange={(e) => setQueryText(e.target.value)}
          style={{ width: '100%', marginBottom: '20px', backgroundColor: '#ffffff' }}
        />
        <Button variant="contained" color="primary" onClick={handleQuerySubmit}>
          Submit
        </Button>
      </div>

      {loading && <CircularProgress style={{ color: '#009688', position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)' }} />}
    </div>
  );
}

export default App;
