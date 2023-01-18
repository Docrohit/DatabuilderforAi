function submitForm() {
  // Get form data
  const data = {
    latitude: document.getElementById('latitude').value,
    longitude: document.getElementById('longitude').value,
    event: document.querySelector('input[name="event"]:checked').value
  };
  // Send POST request to '/runscript' endpoint with form data as request body
  fetch('http://localhost:8000/runscript', {
    method: 'POST',
    body: JSON.stringify(data)
  })
    .then(response => response.text()) // read the response as text
    .then(data => {
      console.log(data); // log the response in the developer console
    });
}
