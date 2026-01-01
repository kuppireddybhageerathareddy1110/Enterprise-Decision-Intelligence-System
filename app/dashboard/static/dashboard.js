let chartInstance = null;

/* -------------------------
   CORE LOADERS
-------------------------- */

async function loadKPIs(symbol, dept = "all") {
  const url = dept === "all" ? "/kpis" : `/kpis/${dept}`;
  const res = await fetch(url);
  const data = await res.json();

  revenue.innerText = symbol + " " + data.total_revenue.toLocaleString();
  profit.innerText = symbol + " " + data.total_profit.toLocaleString();
  department.innerText = dept === "all" ? data.best_department : dept;

  await loadDecisionInsight();   // 🔥 always sync decision
}

async function loadChart() {
  const res = await fetch("/report");
  const data = await res.json();

  const ctx = document.getElementById("revenueChart");

  if (chartInstance) chartInstance.destroy();

  chartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels: data.map(d => d.department),
      datasets: [{
        label: "Profit by Department",
        data: data.map(d => d.profit),
        backgroundColor: "#2563eb"
      }]
    }
  });
}

/* -------------------------
   DECISION INTELLIGENCE
-------------------------- */

async function loadDecisionInsight(extraMessage = "") {
  const res = await fetch("/decision-insight");
  const data = await res.json();

  const el = document.getElementById("decisionMessage");
  el.className = "decision " + data.level;

  el.innerText =
    data.message +
    ` (Margin: ${data.margin}%)` +
    (extraMessage ? ` | ${extraMessage}` : "");
}

async function loadRiskFlags() {
  const res = await fetch("/risk-flags");
  const data = await res.json();

  if (data.count > 0) {
    await loadDecisionInsight(
      `Risk detected in departments: ${data.risk_departments.join(", ")}`
    );
  }
}

/* -------------------------
   USER ACTIONS
-------------------------- */

async function calculate() {
  const payload = {
    revenue: +revenueInput.value,
    cost: +costInput.value,
    employees: +empInput.value
  };

  const res = await fetch("/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await res.json();

  calcResult.innerText =
    `Profit: ₹${data.profit}, Revenue/Employee: ₹${data.revenue_per_employee}`;
}

async function loadFilteredKPIs() {
  const dept = deptFilter.value;
  const config = await fetch("/config").then(r => r.json());
  await loadKPIs(config.currency_symbol, dept);
}

async function compareScenario() {
  const payload = {
    current_revenue: +curRev.value,
    current_cost: +curCost.value,
    scenario_revenue: +scRev.value,
    scenario_cost: +scCost.value
  };

  const res = await fetch("/scenario-compare", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await res.json();

  scenarioResult.innerText =
    `Δ Profit: ₹${data.difference}. ${data.recommendation}`;

  await loadDecisionInsight(data.recommendation);
}

function exportCSV() {
  window.location.href = "/export";
}

/* -------------------------
   APP INIT
-------------------------- */

document.addEventListener("DOMContentLoaded", async () => {
  const config = await fetch("/config").then(r => r.json());

  await loadKPIs(config.currency_symbol);
  await loadChart();
  await loadRiskFlags();

  setInterval(
    () => loadKPIs(config.currency_symbol),
    config.refresh_interval * 1000
  );
});
