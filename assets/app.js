const state = {
  waves: [],
  query: '',
  region: '',
  skill: '',
  showWant: false,
  showHit: false,
  view: 'list',
  checklist: JSON.parse(localStorage.getItem('surfLogChecklist') || '{}')
};

const els = {
  grid: document.querySelector('#wave-grid'),
  summary: document.querySelector('#results-summary'),
  search: document.querySelector('#search'),
  region: document.querySelector('#region-filter'),
  skill: document.querySelector('#skill-filter'),
  showWant: document.querySelector('#show-want'),
  showHit: document.querySelector('#show-hit'),
  viewList: document.querySelector('#view-list'),
  viewMap: document.querySelector('#view-map'),
  mapPanel: document.querySelector('#map-panel'),
  map: document.querySelector('#wave-map'),
  waveCount: document.querySelector('#wave-count'),
  regionCount: document.querySelector('#region-count'),
  waveForm: document.querySelector('#wave-form'),
  formNote: document.querySelector('#form-note')
};

let map;
let markerLayer;

function saveChecklist() {
  localStorage.setItem('surfLogChecklist', JSON.stringify(state.checklist));
}

function checklistFor(id) {
  return state.checklist[id] || { want: false, hit: false };
}

function setChecklist(id, key) {
  const current = checklistFor(id);
  const next = { ...current, [key]: !current[key] };
  if (key === 'hit' && next.hit) next.want = false;
  if (key === 'want' && next.want) next.hit = false;
  state.checklist[id] = next;
  saveChecklist();
  render();
}

function normalized(value) {
  return String(value || '').toLowerCase();
}

function matches(wave) {
  const haystack = normalized([
    wave.name,
    wave.location,
    wave.country,
    wave.region,
    wave.breakType,
    wave.direction,
    wave.bestSeason,
    wave.skillLevel,
    wave.skillNotes,
    wave.whyItBelongs,
    ...(wave.tags || [])
  ].join(' '));
  const check = checklistFor(wave.id);
  return (!state.query || haystack.includes(state.query)) &&
    (!state.region || wave.region === state.region) &&
    (!state.skill || normalized(wave.skillLevel).includes(state.skill)) &&
    (!state.showWant || check.want) &&
    (!state.showHit || check.hit);
}

function allWaves() {
  return state.waves;
}

function waveHasCoordinates(wave) {
  return Number.isFinite(wave.lat) && Number.isFinite(wave.lng) && wave.coordinatePrecision !== 'hidden-unmapped';
}

function renderFilters() {
  const regions = [...new Set(allWaves().map(w => w.region).filter(Boolean))].sort();
  const skills = [...new Set(state.waves.map(w => w.skillLevel).filter(Boolean))].sort();
  els.region.innerHTML = '<option value="">All regions</option>' + regions.map(r => `<option value="${escapeHtml(r)}">${escapeHtml(r)}</option>`).join('');
  els.skill.innerHTML = '<option value="">All skill levels</option>' + skills.map(s => `<option value="${escapeHtml(s.toLowerCase())}">${escapeHtml(s)}</option>`).join('');
  els.waveCount.textContent = allWaves().length;
  els.regionCount.textContent = regions.length;
}

function render() {
  const waves = allWaves();
  const visible = waves.filter(matches);
  const mappedVisible = visible.filter(waveHasCoordinates);

  els.showWant.setAttribute('aria-pressed', String(state.showWant));
  els.showHit.setAttribute('aria-pressed', String(state.showHit));
  els.viewList.setAttribute('aria-pressed', String(state.view === 'list'));
  els.viewMap.setAttribute('aria-pressed', String(state.view === 'map'));
  els.viewList.classList.toggle('active', state.view === 'list');
  els.viewMap.classList.toggle('active', state.view === 'map');
  els.mapPanel.hidden = state.view !== 'map';
  els.grid.hidden = state.view !== 'list';

  els.summary.textContent = state.view === 'map'
    ? `${mappedVisible.length} mapped of ${visible.length} matching waves shown`
    : `${visible.length} of ${waves.length} waves shown`;

  renderCards(visible);
  renderMap(mappedVisible);
}

function renderCards(visible) {
  if (!visible.length) {
    els.grid.innerHTML = '<div class="empty">No waves match that filter yet.</div>';
    return;
  }
  els.grid.innerHTML = visible.map(waveCard).join('');
  els.grid.querySelectorAll('[data-toggle]').forEach(button => {
    button.addEventListener('click', () => setChecklist(button.dataset.id, button.dataset.toggle));
  });
}

function ensureMap() {
  if (!els.map || typeof L === 'undefined') return false;
  if (map) return true;

  map = L.map(els.map, {
    scrollWheelZoom: false,
    worldCopyJump: true
  }).setView([25, -45], 2);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 12,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  markerLayer = L.layerGroup().addTo(map);
  return true;
}

function renderMap(visible) {
  if (state.view !== 'map') return;
  if (!ensureMap()) {
    els.map.innerHTML = '<div class="empty map-empty">Map library failed to load. The list still works.</div>';
    return;
  }

  markerLayer.clearLayers();
  const bounds = [];
  visible.forEach(wave => {
    const marker = L.marker([wave.lat, wave.lng], {
      icon: markerIconFor(wave)
    });
    marker.bindPopup(mapPopup(wave));
    marker.on('popupopen', () => bindPopupButtons(wave.id));
    marker.addTo(markerLayer);
    bounds.push([wave.lat, wave.lng]);
  });

  setTimeout(() => map.invalidateSize(), 0);
  if (bounds.length) {
    map.fitBounds(bounds, { padding: [28, 28], maxZoom: 6 });
  }
}

function markerIconFor(wave) {
  const check = checklistFor(wave.id);
  const stateClass = check.hit ? 'hit' : check.want ? 'want' : 'default';
  return L.divIcon({
    className: `surf-pin surf-pin-${stateClass}`,
    html: '<span></span>',
    iconSize: [24, 24],
    iconAnchor: [12, 12],
    popupAnchor: [0, -12]
  });
}

function mapPopup(wave) {
  const check = checklistFor(wave.id);
  return `
    <div class="map-popup">
      <p class="popup-kicker">${escapeHtml(wave.region || wave.location || '')} · ${escapeHtml(wave.country || '')}</p>
      <h3>${escapeHtml(wave.name)}</h3>
      <p>${escapeHtml(wave.whyItBelongs || '')}</p>
      <p class="popup-note">${escapeHtml(wave.mapNote || 'Approximate public map pin.')}</p>
      <div class="card-actions popup-actions">
        <button class="${check.want ? 'active' : ''}" type="button" data-id="${escapeHtml(wave.id)}" data-toggle="want">Want to hit</button>
        <button class="${check.hit ? 'active' : ''}" type="button" data-id="${escapeHtml(wave.id)}" data-toggle="hit">Hit it</button>
      </div>
    </div>
  `;
}

function bindPopupButtons(id) {
  document.querySelectorAll(`.leaflet-popup [data-id="${CSS.escape(id)}"]`).forEach(button => {
    button.addEventListener('click', () => setChecklist(button.dataset.id, button.dataset.toggle));
  });
}

function waveCard(wave) {
  const check = checklistFor(wave.id);
  const tags = (wave.tags || []).slice(0, 4).map(tag => `<span class="tag">${escapeHtml(tag)}</span>`).join('');
  const mapTag = waveHasCoordinates(wave) ? '<span class="tag">mapped</span>' : '';
  return `
    <article class="wave-card" id="wave-${escapeHtml(wave.id)}">
      <div class="meta">
        <span>${escapeHtml(wave.region || wave.location || '')}</span>
        <span>${escapeHtml(wave.country || '')}</span>
        ${mapTag}
      </div>
      <h3>${escapeHtml(wave.name)}</h3>
      <p>${escapeHtml(wave.whyItBelongs || '')}</p>
      <div class="meta">
        <span>${escapeHtml(wave.breakType || '')}</span>
        <span>${escapeHtml(wave.skillLevel || '')}</span>
      </div>
      <p><strong>Best window:</strong> ${escapeHtml(wave.bestSeason || 'Still being researched')}</p>
      <div class="meta">${tags}</div>
      <div class="card-actions">
        <button class="${check.want ? 'active' : ''}" type="button" data-id="${escapeHtml(wave.id)}" data-toggle="want">Want to hit</button>
        <button class="${check.hit ? 'active' : ''}" type="button" data-id="${escapeHtml(wave.id)}" data-toggle="hit">Hit it</button>
      </div>
    </article>
  `;
}

function escapeHtml(value) {
  return String(value || '').replace(/[&<>'"]/g, char => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#039;', '"': '&quot;'
  }[char]));
}

async function init() {
  const response = await fetch('data/waves.seed.json');
  state.waves = await response.json();
  renderFilters();
  render();
}

function buildWaveSubmissionUrl({ name, region, why }) {
  const title = `Wave suggestion: ${name}`;
  const body = `## Wave name\n${name}\n\n## General region / country\n${region}\n\n## Why it belongs\n${why}\n\n## Best season / window if known\n\n\n## Anything to watch out for\n\n\n## Public source or reference, if any\n\n`;
  const params = new URLSearchParams({
    title,
    labels: 'wave-submission',
    body
  });
  return `https://github.com/jeffreydebolt/the-surf-log/issues/new?${params.toString()}`;
}

els.search.addEventListener('input', event => { state.query = normalized(event.target.value); render(); });
els.region.addEventListener('change', event => { state.region = event.target.value; render(); });
els.skill.addEventListener('change', event => { state.skill = event.target.value; render(); });
els.showWant.addEventListener('click', () => { state.showWant = !state.showWant; render(); });
els.showHit.addEventListener('click', () => { state.showHit = !state.showHit; render(); });
els.viewList.addEventListener('click', () => { state.view = 'list'; render(); });
els.viewMap.addEventListener('click', () => { state.view = 'map'; render(); });
els.waveForm.addEventListener('submit', event => {
  event.preventDefault();
  const form = new FormData(event.currentTarget);
  const name = String(form.get('name') || '').trim();
  const region = String(form.get('region') || '').trim();
  const why = String(form.get('why') || '').trim();
  if (!name || !region || !why) return;
  const url = buildWaveSubmissionUrl({ name, region, why });
  els.formNote.textContent = `Opening the review submission for “${name}”…`;
  window.open(url, '_blank', 'noopener,noreferrer');
});
document.querySelector('[data-action="scroll-submit"]').addEventListener('click', () => {
  document.querySelector('#submit-wave').scrollIntoView({ behavior: 'smooth', block: 'start' });
});

init().catch(error => {
  console.error(error);
  els.grid.innerHTML = '<div class="empty">The wave list failed to load.</div>';
});
