from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app=FastAPI(title='Thermal Console')
SAMPLE={'Sensor':'CPU1','ReadingCelsius':72.0}
def classify_health(reading_celsius):
    """Map a Celsius reading to a ThermalReadingV2 Health value.

    Per contract://thermal/v2: OK <75, Warning 75-84.9, Critical >=85.
    """
    if reading_celsius < 75:
        return 'OK'
    if reading_celsius < 85:
        return 'Warning'
    return 'Critical'
@app.get('/health')
def health(): return {'status':'ok'}
@app.get('/api/thermal')
def thermal():
    reading=SAMPLE['ReadingCelsius']
    return {'Sensor':SAMPLE['Sensor'],'ReadingCelsius':reading,'Health':classify_health(reading)}
@app.get('/',response_class=HTMLResponse)
def home():
    return HTMLResponse('''<!doctype html><html><head><meta charset='utf-8'><title>Thermal Console</title><style>body{font-family:Arial;margin:40px}.badge{padding:6px 10px;border-radius:14px;background:#ddd;color:#000}.badge.ok{background:#1e7e34;color:#fff}.badge.warning{background:#e0a800;color:#000}.badge.critical{background:#c82333;color:#fff}</style></head><body><h1>Thermal Console</h1><p>Sensor: <span id='sensor'></span></p><p>Reading: <span id='reading'></span> °C</p><span id='health' class='badge'>Unknown</span><script>fetch('/api/thermal').then(r=>r.json()).then(x=>{sensor.textContent=x.Sensor;reading.textContent=x.ReadingCelsius;var h=document.getElementById('health');h.textContent=x.Health;h.className='badge '+x.Health.toLowerCase();});</script></body></html>''')
