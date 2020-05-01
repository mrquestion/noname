import React, { useEffect, useRef, useState } from 'react';

import './App.css';

import bent from 'bent';

function App() {
  const api = {
    head: bent(window.location.origin, 'json', 'HEAD'),
    put: bent(window.location.origin, 'json', 'PUT'),
    post: bent(window.location.origin, 'json', 'POST'),
    get: bent(window.location.origin, 'json', 'GET'),
    patch: bent(window.location.origin, 'json', 'PATCH'),
    delete: bent(window.location.origin, 'json', 'DELETE'),
  };

  useEffect(() => {
    api.get('/api/v1/version').then(({ error, version }) => {
      console.log('API version:', version)
    });
  }, []);

  return (
    <div className="container-fluid">
      <div className="row">
        <div className="col col-12">
          noname
        </div>
      </div>
    </div>
  );
}

export default App;
