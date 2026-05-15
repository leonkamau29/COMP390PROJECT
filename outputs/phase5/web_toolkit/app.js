const DATA_SOURCES = {
  taxonomy: "../../../outputs/phase1/capability_taxonomy_FINAL.csv",
  benchmarks: "../../../data/phase2/benchmark_database.csv",
  coverage: "../../../data/phase3/coverage_matrix.csv",
  gaps: "../../../data/phase3/gap_scores.csv",
};

const USE_CASE_TEMPLATES = [
  {
    id: "custom",
    name: "Custom use case",
    note: "Set your own capability priorities.",
    weights: {},
  },
  {
    id: "coding",
    name: "Coding assistant",
    note: "Software development, debugging, refactoring, and technical problem solving.",
    weights: { C02: 5, C03: 2, C05: 2, C07: 1 },
  },
  {
    id: "education",
    name: "Education tutor",
    note: "Tutoring, explanation, scaffolding, and academic support.",
    weights: { C04: 5, C03: 3, C05: 2, C01: 1 },
  },
  {
    id: "writing",
    name: "Writing assistant",
    note: "Drafting, editing, content improvement, and communication.",
    weights: { C01: 5, C05: 4, C03: 2, C06: 1 },
  },
  {
    id: "knowledge",
    name: "Knowledge assistant",
    note: "Question answering, recommendations, and grounded advisory work.",
    weights: { C03: 5, C07: 3, C05: 1 },
  },
  {
    id: "data",
    name: "Data analysis assistant",
    note: "Summarisation, document analysis, reporting, and analytical workflows.",
    weights: { C07: 5, C03: 3, C02: 2, C01: 1 },
  },
  {
    id: "multilingual",
    name: "Multilingual assistant",
    note: "Translation, cross-lingual work, and multilingual communication.",
    weights: { C06: 5, C01: 2, C03: 2, C05: 1 },
  },
  {
    id: "roleplay",
    name: "Conversation and roleplay",
    note: "Interactive dialogue, roleplay, social practice, and support contexts.",
    weights: { C08: 5, C01: 2, C04: 1, C05: 1 },
  },
];

const state = {
  capabilities: [],
  benchmarks: [],
  coverageRows: [],
  gaps: [],
  weights: {},
  selectedTemplate: "custom",
};

function parseCSV(text) {
  const rows = [];
  let current = "";
  let row = [];
  let insideQuotes = false;

  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    const nextChar = text[i + 1];

    if (char === '"' && insideQuotes && nextChar === '"') {
      current += '"';
      i += 1;
    } else if (char === '"') {
      insideQuotes = !insideQuotes;
    } else if (char === "," && !insideQuotes) {
      row.push(current);
      current = "";
    } else if ((char === "\n" || char === "\r") && !insideQuotes) {
      if (char === "\r" && nextChar === "\n") {
        i += 1;
      }
      row.push(current);
      if (row.some((value) => value.trim() !== "")) {
        rows.push(row);
      }
      current = "";
      row = [];
    } else {
      current += char;
    }
  }

  if (current.length > 0 || row.length > 0) {
    row.push(current);
    rows.push(row);
  }

  const [headers, ...records] = rows;
  return records.map((record) => {
    const item = {};
    headers.forEach((header, index) => {
      item[header] = record[index] ?? "";
    });
    return item;
  });
}

async function loadCSV(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Failed to load ${path}`);
  }
  return parseCSV(await response.text());
}

function numberValue(value, fallback = 0) {
  const parsed = Number.parseFloat(value);
  return Number.isFinite(parsed) ? parsed : fallback;
}

function byId(id) {
  return document.getElementById(id);
}

function escapeHTML(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function capabilityById(capabilityId) {
  return state.capabilities.find((capability) => capability.capability_id === capabilityId);
}

function coverageForBenchmark(benchmarkId) {
  return state.coverageRows.find((row) => row.benchmark_id === benchmarkId) ?? {};
}

function capabilityGap(capabilityId) {
  return state.gaps.find((gap) => gap.capability_id === capabilityId) ?? {};
}

function activeCapabilityIds() {
  return state.capabilities
    .map((capability) => capability.capability_id)
    .filter((capabilityId) => (state.weights[capabilityId] ?? 0) > 0);
}

function maxRatingForCapability(capabilityId) {
  return Math.max(
    0,
    ...state.coverageRows.map((row) => numberValue(row[capabilityId]))
  );
}

function averageQuality(benchmark) {
  const values = [
    benchmark.quality_coherence,
    benchmark.quality_accuracy,
    benchmark.quality_clarity,
    benchmark.quality_relevance,
    benchmark.quality_efficiency,
  ].map((value) => numberValue(value)).filter((value) => value > 0);

  if (!values.length) {
    return 0;
  }

  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

function benchmarkMatchScore(benchmark) {
  const coverage = coverageForBenchmark(benchmark.benchmark_id);
  let weightedScore = 0;
  let possibleScore = 0;

  state.capabilities.forEach((capability) => {
    const weight = state.weights[capability.capability_id] ?? 0;
    if (weight > 0) {
      weightedScore += weight * numberValue(coverage[capability.capability_id]);
      possibleScore += weight * 5;
    }
  });

  return possibleScore > 0 ? (weightedScore / possibleScore) * 100 : 0;
}

function ecosystemCoverageScore() {
  let weightedScore = 0;
  let possibleScore = 0;

  state.capabilities.forEach((capability) => {
    const weight = state.weights[capability.capability_id] ?? 0;
    if (weight > 0) {
      weightedScore += weight * maxRatingForCapability(capability.capability_id);
      possibleScore += weight * 5;
    }
  });

  return possibleScore > 0 ? (weightedScore / possibleScore) * 100 : 0;
}

function rankedBenchmarks() {
  return state.benchmarks
    .map((benchmark) => ({
      ...benchmark,
      matchScore: benchmarkMatchScore(benchmark),
      qualityAverage: averageQuality(benchmark),
    }))
    .sort((a, b) => {
      if (b.matchScore !== a.matchScore) {
        return b.matchScore - a.matchScore;
      }
      return b.qualityAverage - a.qualityAverage;
    });
}

function severityTone(score) {
  if (score >= 80) return "success";
  if (score >= 60) return "warning";
  return "danger";
}

function contaminationTone(value) {
  const lower = String(value).toLowerCase();
  if (lower.includes("high")) return "danger";
  if (lower.includes("medium")) return "warning";
  if (lower.includes("low")) return "success";
  return "";
}

function shortName(name, maxLength = 42) {
  if (!name || name.length <= maxLength) return name;
  return `${name.slice(0, maxLength - 1)}...`;
}

function setTemplate(templateId) {
  const template = USE_CASE_TEMPLATES.find((item) => item.id === templateId);
  state.selectedTemplate = templateId;
  state.weights = {};

  state.capabilities.forEach((capability) => {
    state.weights[capability.capability_id] = template?.weights[capability.capability_id] ?? 0;
  });

  byId("use-case-notes").value = template?.id === "custom" ? "" : template?.note ?? "";
  renderTemplateButtons();
  renderSliders();
  updateCalculator();
}

function renderTemplateButtons() {
  byId("template-buttons").innerHTML = USE_CASE_TEMPLATES.map((template) => `
    <button
      class="template-button ${template.id === state.selectedTemplate ? "active" : ""}"
      data-template="${template.id}"
      type="button"
    >
      ${escapeHTML(template.name)}
    </button>
  `).join("");

  document.querySelectorAll("[data-template]").forEach((button) => {
    button.addEventListener("click", () => setTemplate(button.dataset.template));
  });
}

function renderSliders() {
  byId("capability-sliders").innerHTML = state.capabilities.map((capability) => {
    const gap = capabilityGap(capability.capability_id);
    const value = state.weights[capability.capability_id] ?? 0;
    return `
      <div class="slider-row">
        <div>
          <div class="cap-title">${escapeHTML(capability.capability_name)}</div>
          <div class="cap-meta">
            ${escapeHTML(capability.capability_id)} -
            usage ${numberValue(gap.usage_pct).toFixed(1)}% -
            gap rank ${escapeHTML(gap.gap_rank || "n/a")}
          </div>
        </div>
        <input
          type="range"
          min="0"
          max="5"
          step="1"
          value="${value}"
          data-weight="${escapeHTML(capability.capability_id)}"
          aria-label="Weight for ${escapeHTML(capability.capability_name)}"
        >
        <span class="weight-value" id="weight-${escapeHTML(capability.capability_id)}">${value}</span>
      </div>
    `;
  }).join("");

  document.querySelectorAll("[data-weight]").forEach((input) => {
    input.addEventListener("input", () => {
      state.selectedTemplate = "custom";
      state.weights[input.dataset.weight] = Number.parseInt(input.value, 10);
      byId(`weight-${input.dataset.weight}`).textContent = input.value;
      renderTemplateButtons();
      updateCalculator();
    });
  });
}

function interpretationFor(score) {
  if (score >= 80) {
    return "Strong fit: the analysed benchmark inventory contains good coverage for the selected use case. Inspect limitations before relying on any single benchmark.";
  }
  if (score >= 60) {
    return "Moderate fit: use multiple benchmarks and check capability-specific gaps before making deployment claims.";
  }
  if (score >= 40) {
    return "Weak fit: existing benchmarks only partially represent this use case. Supplementary evaluation is recommended.";
  }
  if (score > 0) {
    return "Poor fit: the selected use case is not well covered by the analysed benchmark inventory. A custom or adapted benchmark is likely needed.";
  }
  return "Select at least one capability to calculate a recommendation.";
}

function renderRecommendationBars(benchmarks) {
  const topBenchmarks = benchmarks.filter((benchmark) => benchmark.matchScore > 0).slice(0, 6);
  if (!topBenchmarks.length) {
    byId("recommendation-bars").innerHTML = `<p class="hint">No weighted capabilities selected yet.</p>`;
    return;
  }

  byId("recommendation-bars").innerHTML = topBenchmarks.map((benchmark) => `
    <div class="bar-item">
      <div class="bar-top">
        <strong>${escapeHTML(shortName(benchmark.name))}</strong>
        <span>${benchmark.matchScore.toFixed(0)}%</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill ${severityTone(benchmark.matchScore)}" style="width: ${benchmark.matchScore}%"></div>
      </div>
      <div class="badge-row">
        <span class="badge">Quality ${benchmark.qualityAverage.toFixed(1)}/5</span>
        <span class="badge ${contaminationTone(benchmark.contamination_risk)}">${escapeHTML(benchmark.contamination_risk.split(" - ")[0])}</span>
        <span class="badge">${escapeHTML(benchmark.primary_capability)}</span>
      </div>
    </div>
  `).join("");
}

function renderGapBreakdown() {
  const active = activeCapabilityIds();
  if (!active.length) {
    byId("gap-breakdown").innerHTML = `<p class="hint">Capability gap drivers will appear here after weights are selected.</p>`;
    return;
  }

  const rows = active.map((capabilityId) => {
    const capability = capabilityById(capabilityId);
    const bestRating = maxRatingForCapability(capabilityId);
    const weight = state.weights[capabilityId] ?? 0;
    const risk = ((5 - bestRating) / 5) * weight;
    const gap = capabilityGap(capabilityId);
    return {
      capability,
      bestRating,
      weight,
      risk,
      gap,
    };
  }).sort((a, b) => b.risk - a.risk);

  byId("gap-breakdown").innerHTML = rows.map((row) => `
    <div class="gap-item">
      <strong>${escapeHTML(row.capability.capability_name)}</strong>
      <span>
        User weight ${row.weight}/5, best available coverage ${row.bestRating}/5,
        Phase 3 severity ${escapeHTML(row.gap.severity || "n/a")}.
      </span>
    </div>
  `).join("");
}

function greedyBenchmarkSet() {
  const active = activeCapabilityIds();
  if (!active.length) {
    return [];
  }

  const selected = [];
  const selectedIds = new Set();
  const currentCoverage = Object.fromEntries(active.map((capabilityId) => [capabilityId, 0]));

  for (let round = 0; round < 4; round += 1) {
    let bestCandidate = null;
    let bestGain = 0;

    state.benchmarks.forEach((benchmark) => {
      if (selectedIds.has(benchmark.benchmark_id)) {
        return;
      }

      const coverage = coverageForBenchmark(benchmark.benchmark_id);
      const gain = active.reduce((sum, capabilityId) => {
        const rating = numberValue(coverage[capabilityId]);
        const improvement = Math.max(0, rating - currentCoverage[capabilityId]);
        return sum + improvement * (state.weights[capabilityId] ?? 0);
      }, 0);

      if (gain > bestGain) {
        bestGain = gain;
        bestCandidate = benchmark;
      }
    });

    if (!bestCandidate) {
      break;
    }

    selected.push({ ...bestCandidate, gain: bestGain });
    selectedIds.add(bestCandidate.benchmark_id);
    const coverage = coverageForBenchmark(bestCandidate.benchmark_id);
    active.forEach((capabilityId) => {
      currentCoverage[capabilityId] = Math.max(
        currentCoverage[capabilityId],
        numberValue(coverage[capabilityId])
      );
    });
  }

  return selected;
}

function renderBenchmarkSet() {
  const set = greedyBenchmarkSet();
  if (!set.length) {
    byId("benchmark-set").innerHTML = `<p class="hint">Select capabilities to generate a suggested benchmark set.</p>`;
    return;
  }

  byId("benchmark-set").innerHTML = set.map((benchmark) => `
    <article class="card">
      <p class="eyebrow">${escapeHTML(benchmark.benchmark_id)}</p>
      <h3>${escapeHTML(benchmark.name)}</h3>
      <p>${escapeHTML(benchmark.task_type)}</p>
      <div class="meta-grid">
        <div class="meta"><span>Primary</span>${escapeHTML(benchmark.primary_capability)}</div>
        <div class="meta"><span>Quality</span>${averageQuality(benchmark).toFixed(1)}/5</div>
      </div>
      <p class="hint">${escapeHTML(benchmark.known_limitations)}</p>
    </article>
  `).join("");
}

function updateCalculator() {
  const score = ecosystemCoverageScore();
  const risk = score > 0 ? 100 - score : 0;
  const ranked = rankedBenchmarks();

  byId("coverage-score").textContent = `${score.toFixed(0)}%`;
  byId("gap-risk").textContent = `${risk.toFixed(0)}%`;
  byId("result-interpretation").textContent = interpretationFor(score);

  renderRecommendationBars(ranked);
  renderGapBreakdown();
  renderBenchmarkSet();
}

function renderCapabilityCards() {
  const sorted = [...state.capabilities].sort((a, b) => {
    const gapA = numberValue(capabilityGap(a.capability_id).gap_rank, 99);
    const gapB = numberValue(capabilityGap(b.capability_id).gap_rank, 99);
    return gapA - gapB;
  });

  byId("capability-cards").innerHTML = sorted.map((capability) => {
    const gap = capabilityGap(capability.capability_id);
    return `
      <article class="card">
        <p class="eyebrow">${escapeHTML(capability.capability_id)}</p>
        <h3>${escapeHTML(capability.capability_name)}</h3>
        <p>${escapeHTML(capability.definition)}</p>
        <div class="meta-grid">
          <div class="meta"><span>Usage</span>${numberValue(gap.usage_pct).toFixed(1)}%</div>
          <div class="meta"><span>Coverage</span>${(numberValue(gap.total_coverage_score) * 100).toFixed(0)}%</div>
          <div class="meta"><span>Gap score</span>${numberValue(gap.gap_score).toFixed(3)}</div>
          <div class="meta"><span>Rank</span>${escapeHTML(gap.gap_rank || "n/a")}</div>
        </div>
        <div class="badge-row">
          <span class="badge ${String(gap.severity).toLowerCase()}">${escapeHTML(gap.severity || "Unrated")}</span>
        </div>
      </article>
    `;
  }).join("");
}

function renderBenchmarkFilter() {
  byId("capability-filter").innerHTML = `
    <option value="all">All capabilities</option>
    ${state.capabilities.map((capability) => `
      <option value="${escapeHTML(capability.capability_id)}">
        ${escapeHTML(capability.capability_id)} - ${escapeHTML(capability.capability_name)}
      </option>
    `).join("")}
  `;
}

function renderBenchmarkCards() {
  const query = byId("benchmark-search").value.trim().toLowerCase();
  const capabilityFilter = byId("capability-filter").value;

  const filtered = state.benchmarks.filter((benchmark) => {
    const coverage = coverageForBenchmark(benchmark.benchmark_id);
    const matchesCapability = capabilityFilter === "all" || numberValue(coverage[capabilityFilter]) > 0;
    const haystack = [
      benchmark.name,
      benchmark.abbreviation,
      benchmark.domain,
      benchmark.task_type,
      benchmark.known_limitations,
      benchmark.quality_notes,
    ].join(" ").toLowerCase();

    return matchesCapability && (!query || haystack.includes(query));
  });

  byId("benchmark-cards").innerHTML = filtered.map((benchmark) => {
    const coverage = coverageForBenchmark(benchmark.benchmark_id);
    const coveredCapabilities = state.capabilities
      .filter((capability) => numberValue(coverage[capability.capability_id]) > 0)
      .map((capability) => `${capability.capability_id}:${coverage[capability.capability_id]}`);

    return `
      <article class="card">
        <p class="eyebrow">${escapeHTML(benchmark.benchmark_id)} - ${escapeHTML(benchmark.abbreviation)}</p>
        <h3>${escapeHTML(benchmark.name)}</h3>
        <p>${escapeHTML(benchmark.task_type)}. ${escapeHTML(benchmark.domain)}</p>
        <div class="meta-grid">
          <div class="meta"><span>Year</span>${escapeHTML(benchmark.year)}</div>
          <div class="meta"><span>Quality</span>${averageQuality(benchmark).toFixed(1)}/5</div>
          <div class="meta"><span>Availability</span>${escapeHTML(benchmark.public_availability)}</div>
          <div class="meta"><span>Update</span>${escapeHTML(benchmark.update_frequency)}</div>
        </div>
        <p class="hint">${escapeHTML(benchmark.known_limitations)}</p>
        <div class="badge-row">
          <span class="badge ${contaminationTone(benchmark.contamination_risk)}">${escapeHTML(benchmark.contamination_risk.split(" - ")[0])}</span>
          ${coveredCapabilities.map((item) => `<span class="badge">${escapeHTML(item)}</span>`).join("")}
        </div>
      </article>
    `;
  }).join("") || `<p class="hint">No benchmarks match the current filters.</p>`;
}

function renderGapChart() {
  const maxGap = Math.max(0, ...state.gaps.map((gap) => numberValue(gap.gap_score)));
  byId("gap-chart").innerHTML = [...state.gaps]
    .sort((a, b) => numberValue(a.gap_rank) - numberValue(b.gap_rank))
    .map((gap) => {
      const width = maxGap > 0 ? (numberValue(gap.gap_score) / maxGap) * 100 : 0;
      return `
        <div class="bar-item">
          <div class="bar-top">
            <strong>${escapeHTML(gap.capability_name)}</strong>
            <span>${numberValue(gap.gap_score).toFixed(3)}</span>
          </div>
          <div class="bar-track">
            <div class="bar-fill ${String(gap.severity).toLowerCase()}" style="width: ${width}%"></div>
          </div>
        </div>
      `;
    }).join("");
}

function renderScatter() {
  const width = 520;
  const height = 320;
  const padding = 44;
  const maxUsage = Math.max(...state.gaps.map((gap) => numberValue(gap.usage_frequency)));
  const maxCoverage = Math.max(...state.gaps.map((gap) => numberValue(gap.total_coverage_score)));

  const points = state.gaps.map((gap) => {
    const usage = numberValue(gap.usage_frequency);
    const coverage = numberValue(gap.total_coverage_score);
    const x = padding + (usage / maxUsage) * (width - padding * 2);
    const y = height - padding - (coverage / maxCoverage) * (height - padding * 2);
    return `
      <circle cx="${x}" cy="${y}" r="5" fill="currentColor"></circle>
      <text x="${Math.min(x + 8, width - 130)}" y="${y - 6}">${escapeHTML(gap.capability_id)}</text>
    `;
  }).join("");

  byId("scatter-plot").innerHTML = `
    <svg viewBox="0 0 ${width} ${height}" role="img" aria-label="Usage frequency versus coverage score scatter plot">
      <line x1="${padding}" y1="${height - padding}" x2="${width - padding}" y2="${height - padding}" stroke="currentColor" opacity="0.25"></line>
      <line x1="${padding}" y1="${padding}" x2="${padding}" y2="${height - padding}" stroke="currentColor" opacity="0.25"></line>
      <text x="${width / 2 - 45}" y="${height - 10}">Usage frequency</text>
      <text x="8" y="24">Coverage</text>
      <g style="color: var(--accent)">${points}</g>
    </svg>
  `;
}

function renderHeatmap() {
  const headers = state.capabilities.map((capability) => capability.capability_id);
  byId("heatmap").innerHTML = `
    <table class="heatmap">
      <thead>
        <tr>
          <th>Benchmark</th>
          ${headers.map((header) => `<th>${escapeHTML(header)}</th>`).join("")}
        </tr>
      </thead>
      <tbody>
        ${state.benchmarks.map((benchmark) => {
          const coverage = coverageForBenchmark(benchmark.benchmark_id);
          return `
            <tr>
              <td>${escapeHTML(benchmark.abbreviation || benchmark.name)}</td>
              ${headers.map((header) => {
                const rating = numberValue(coverage[header]);
                return `<td><span class="heat-cell heat-${rating}">${rating}</span></td>`;
              }).join("")}
            </tr>
          `;
        }).join("")}
      </tbody>
    </table>
  `;
}

function wireTabs() {
  document.querySelectorAll(".tab").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".tab").forEach((tab) => tab.classList.remove("active"));
      document.querySelectorAll(".view").forEach((view) => view.classList.remove("active"));
      button.classList.add("active");
      byId(button.dataset.view).classList.add("active");
    });
  });
}

function wireFilters() {
  byId("benchmark-search").addEventListener("input", renderBenchmarkCards);
  byId("capability-filter").addEventListener("change", renderBenchmarkCards);
  byId("reset-weights").addEventListener("click", () => setTemplate("custom"));
}

function renderAll() {
  renderTemplateButtons();
  renderSliders();
  renderCapabilityCards();
  renderBenchmarkFilter();
  renderBenchmarkCards();
  renderGapChart();
  renderScatter();
  renderHeatmap();
  updateCalculator();
}

async function initialise() {
  wireTabs();
  wireFilters();

  try {
    const [taxonomy, benchmarks, coverageRows, gaps] = await Promise.all([
      loadCSV(DATA_SOURCES.taxonomy),
      loadCSV(DATA_SOURCES.benchmarks),
      loadCSV(DATA_SOURCES.coverage),
      loadCSV(DATA_SOURCES.gaps),
    ]);

    state.capabilities = taxonomy;
    state.benchmarks = benchmarks;
    state.coverageRows = coverageRows;
    state.gaps = gaps;

    setTemplate("custom");
    renderAll();

    const loadState = byId("load-state");
    loadState.className = "notice success";
    loadState.textContent = `Loaded ${state.benchmarks.length} benchmarks and ${state.capabilities.length} capabilities from the project evidence files.`;
  } catch (error) {
    const loadState = byId("load-state");
    loadState.className = "notice error";
    loadState.textContent = `${error.message}. Run the toolkit from the project root with a local server, for example: python -m http.server 8000`;
  }
}

initialise();
