// frontend/js/dashboard.js

$(document).ready(function () {
    loadStats();
    loadSpending();
    loadTrend();
    loadFraud();
    loadFraudHeatmap();
    loadPrediction();
    loadClusters();
    simulateTraining();
});

/* ================================
   Currency Formatter
================================ */
function formatINR(amount) {
    return (
        "₹" +
        Number(amount).toLocaleString("en-IN", {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
        })
    );
}

/* ================================
   Dataset Statistics
================================ */
function loadStats() {
    $.get("/stats", function (data) {
        $("#statTransactions").html(data.transactions.toLocaleString("en-IN"));
        $("#metricTransactions").html(data.transactions.toLocaleString("en-IN"));
        $("#statAmount").html(formatINR(data.spending));
        $("#statCategories").html(data.categories);
        $("#statMerchants").html(data.merchants);
        $("#metricUsers").html(data.users);
    }).fail(function () {
        $("#statTransactions").html("--");
        $("#metricTransactions").html("--");
        $("#statAmount").html("--");
        $("#statCategories").html("--");
        $("#statMerchants").html("--");
        $("#metricUsers").html("--");
    });
    /***
    $.get("/analytics/spending", function (data) {
        const total = Object.values(data).reduce(function (a, b) {
            return a + b;
        }, 0);

        $("#statTransactions").html("100,000");
        $("#statAmount").html(formatINR(total));
        $("#statCategories").html(Object.keys(data).length);
        $("#statMerchants").html("~500");
    }).fail(function () {
        $("#statTransactions").html("--");
        $("#statAmount").html("--");
        $("#statCategories").html("--");
        $("#statMerchants").html("--");
    });
    ***/
}

/* ================================
   Simulate Model Training Progress
================================ */
function simulateTraining() {
    let progress = 0;
    const interval = setInterval(function () {
        progress += 10;
        if (progress > 100) {
            progress = 100;
        }
        $("#trainingBar").css("width", progress + "%");
        if (progress >= 100) {
            $("#trainingStatus").text("Models Trained");
            clearInterval(interval);
        }
    }, 200);
}

/* ================================
   Spending Trend (Animated Line)
================================ */
function loadTrend() {
    $.get("/analytics/spending", function (data) {
        const labels = Object.keys(data);
        const values = Object.values(data);

        const ctx = document.getElementById("trendChart").getContext("2d");
        new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [{
                    label: "Spending Trend",
                    data: values,
                    borderColor: "#16a34a",
                    backgroundColor: "rgba(22,163,74,0.05)",
                    tension: 0.35,
                    fill: true,
                }, ],
            },
            options: {
                animation: {
                    duration: 2000,
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                return formatINR(context.raw);
                            },
                        },
                    },
                },
                scales: {
                    y: {
                        ticks: {
                            callback: function (value) {
                                return formatINR(value);
                            },
                        },
                    },
                },
            },
        });
    }).fail(function () {
        // no-op on fail
    });
}

/* ================================
   Aggregated Spending (Bar Chart)
================================ */
function loadSpending() {
    $.get("/analytics/spending", function (data) {
        const labels = Object.keys(data);
        const values = Object.values(data);

        const ctx = document.getElementById("spendingChart").getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Total Spending",
                    data: values,
                    backgroundColor: "#3b82f6",
                }, ],
            },
            options: {
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                return formatINR(context.raw);
                            },
                        },
                    },
                },
                scales: {
                    y: {
                        ticks: {
                            callback: function (value) {
                                return formatINR(value);
                            },
                        },
                    },
                },
            },
        });
    }).fail(function () {
        // no-op
    });
}

/* ================================
   Anomaly / Fraud Table
================================ */
function loadFraud() {
    $.get("/analytics/fraud", function (data) {
        let html =
            "<thead><tr class='bg-gray-200'><th class='p-2'>User</th><th class='p-2'>Merchant</th><th class='p-2'>Amount</th></tr></thead><tbody>";

        const users = new Set();

        if (Array.isArray(data) && data.length > 0) {
            data.forEach(function (row) {
                users.add(row.user_id);
                html += "<tr>";
                html += "<td class='p-2'>" + (row.user_id || "--") + "</td>";
                html += "<td class='p-2'>" + (row.merchant || "--") + "</td>";
                html +=
                    "<td class='p-2'>" + (row.amount !== undefined ? formatINR(row.amount) : "--") + "</td>";
                html += "</tr>";
            });
        } else {
            html += "<tr><td class='p-2' colspan='3'>No anomalies detected</td></tr>";
        }

        html += "</tbody>";
        $("#fraudTable").html(html);

        $("#metricUsers").html(users.size);
        $("#metricFraud").html(Array.isArray(data) ? data.length : 0);
    }).fail(function () {
        $("#fraudTable").html("<tr><td colspan='3'>Error loading anomalies</td></tr>");
        $("#metricUsers").html("--");
        $("#metricFraud").html("--");
    });
}

/* ================================
   Fraud Probability Heatmap (Bar)
================================ */
function loadFraudHeatmap() {
    $.get("/analytics/fraud", function (data) {
        const labels = [];
        const values = [];

        if (Array.isArray(data) && data.length > 0) {
            data.forEach(function (row) {
                labels.push(row.merchant || "unknown");
                values.push(row.amount || 0);
            });
        }

        const ctx = document.getElementById("fraudHeatmap").getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Fraud Risk",
                    data: values,
                    backgroundColor: "#ef4444",
                }, ],
            },
            options: {
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                return formatINR(context.raw);
                            },
                        },
                    },
                },
                scales: {
                    y: {
                        ticks: {
                            callback: function (value) {
                                return formatINR(value);
                            },
                        },
                    },
                },
            },
        });
    }).fail(function () {
        // no-op
    });
}

/* ================================
   Spending Prediction (Next Transaction)
================================ */
function loadPrediction() {
    $.get("/analytics/predict", function (data) {
        if (data && typeof data.prediction !== "undefined") {
            $("#metricPrediction").html(formatINR(data.prediction));
        } else {
            $("#metricPrediction").html("--");
        }
    }).fail(function () {
        $("#metricPrediction").html("--");
    });
}

/* ================================
   Category Prediction (form)
================================ */
$("#predictBtn").click(function () {
    const merchant = $("#merchant").val();
    const amount = $("#amount").val();

    $.get("/analytics/predict-category", {
        merchant: merchant,
        amount: amount
    }, function (data) {
        if (data && data.category) {
            $("#categoryResult").html("Predicted Category: <b>" + data.category + "</b>");
        } else {
            $("#categoryResult").html("Predicted Category: <b>--</b>");
        }
    }).fail(function () {
        $("#categoryResult").html("Error predicting category");
    });
});

/* ================================
   User Segmentation (Scatter)
================================ */
function loadClusters() {
    $.get("/analytics/cluster", function (data) {
        const points = [];

        if (Array.isArray(data) && data.length > 0) {
            data.forEach(function (row, index) {
                // Ensure y is a number
                const y = typeof row.amount === "number" ? row.amount : Number(row.amount) || 0;
                points.push({
                    x: index,
                    y: y,
                });
            });
        }

        const ctx = document.getElementById("clusterChart").getContext("2d");
        new Chart(ctx, {
            type: "scatter",
            data: {
                datasets: [{
                    label: "User Segments",
                    data: points,
                    backgroundColor: "#ef4444",
                }, ],
            },
            options: {
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                if (context.raw && typeof context.raw.y !== "undefined") {
                                    return formatINR(context.raw.y);
                                }
                                return "";
                            },
                        },
                    },
                },
                scales: {
                    y: {
                        ticks: {
                            callback: function (value) {
                                return formatINR(value);
                            },
                        },
                    },
                },
            },
        });
    }).fail(function () {
        // no-op
    });
}