document.getElementById('searchForm').addEventListener('submit', async function (event) {
  event.preventDefault();
  
  const city = document.getElementById('city').value;
  const response = await fetch(`/wetter?stadt=${city}`);
  const data = await response.json();
  
  const resultDiv = document.getElementById('meldung');
  
  if (response.ok) {
    const weather = data.weather[0].description;
    const temp = data.main.temp;

    resultDiv.innerHTML = 
      `<p><strong>Wetter in ${data.name}:</strong></p>
       <p>🌡️ Temperatur: ${temp}°C</p>
       <p>☁️ Zustand: ${weather}</p>`;
  } else {
    resultDiv.innerHTML = 
      `<p style="color:red;">Fehler: ${data.error || "Keine Daten gefunden"}</p>`;
  }
});

