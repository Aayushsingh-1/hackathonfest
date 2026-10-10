<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Customer Retention Predictor</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Google Fonts Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
     body { font-family: 'Inter', sans-serif; }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col">

    <!-- Header -->
    <header class="bg-indigo-900 text-white shadow-lg">
        <div class="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-4">
            <div class="flex items-center space-x-3">
                <div class="p-2.5 bg-indigo-700 rounded-xl shadow-inner flex items-center justify-center">
                    <i data-lucide="brain-circuit" class="w-8 h-8 text-indigo-200"></i>
                </div>
                <h1 class="text-2xl font-bold tracking-tight">E-Commerce Customer Retention Predictor</h1>
                    <p class="text-indigo-200 text-sm">Powered by scikit-learn Random Forest Simulation & Rule Engine</p>
                </div>
            </div>
            <div class="flex items-center gap-3 bg-indigo-800/80 px-4 py-2 rounded-xl border border-indigo-700">
                <i data-lucide="database" class="w-5 h-5 text-indigo-300"></i>
                <span class="text-sm font-medium">Dataset Records: <strong id="total-records" class="text-white">12</strong> Users</span>
            </div>
        </div>
    </header>!-- Main Container -->
    <main class="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8 flex-grow w-full space-y-8">

        <!-- Metrics Overview Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200/80 flex items-center justify-between">
                <div>
                    <p class="text-xs font-semibold uppercase tracking-wider text-slate-400">Total Users</p>
                    <h3 id="stat-total" class="text-3xl font-bold text-slate-900 mt-1">12</h3>
                </div>
                   <h3 id="stat-total" class="text-3xl font-bold text-slate-900 mt-1">12</h3>
                </div>
                <div class="p-3 bg-blue-50 text-blue-600 rounded-xl">
                    <i data-lucide="users" class="w-6 h-6"></i>
                </div>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200/80 flex items-center justify-between">
                <div>
                    <p class="text-xs font-semibold uppercase tracking-wider text-slate-400">Predicted Stays (1)</p>
                    <h3 id="stat-stays" class="text-3xl font-bold text-emerald-600 mt-1">0</h3>
                </div>
                <div class="p-3 bg-emerald-50 text-emerald-600 rounded-xl">
                    <i data-lucide="user-check" class="w-6 h-6"></i>
                     </div>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200/80 flex items-center justify-between">
                <div>
                    <p class="text-xs font-semibold uppercase tracking-wider text-slate-400">Predicted Leaves (0)</p>
                    <h3 id="stat-leaves" class="text-3xl font-bold text-rose-600 mt-1">0</h3>
                </div>
                <div class="p-3 bg-rose-50 text-rose-600 rounded-xl">
                    <i data-lucide="user-x" class="w-6 h-6"></i>
                </div>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200/80 flex items-center justify-between">
             <div>
                    <p class="text-xs font-semibold uppercase tracking-wider text-slate-400">Retention Rate</p>
                    <h3 id="stat-rate" class="text-3xl font-bold text-indigo-600 mt-1">0%</h3>
                </div>
                <div class="p-3 bg-indigo-50 text-indigo-600 rounded-xl">
                    <i data-lucide="trending-up" class="w-6 h-6"></i>
                </div>
            </div>
        </div>
 <!-- Interactive Tabs Navigation -->
        <div class="flex border-b border-slate-200 space-x-6">
            <button onclick="switchTab('dashboard')" id="tab-btn-dashboard" class="pb-3 border-b-2 font-semibold text-sm transition-all border-indigo-600 text-indigo-600 flex items-center gap-2">
                <i data-lucide="layout-dashboard" class="w-4 h-4"></i> Dataset Dashboard
            </button>
            <button onclick="switchTab('lookup')" id="tab-btn-lookup" class="pb-3 border-b-2 font-medium text-sm transition-all border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2">
                <i data-lucide="search" class="w-4 h-4"></i> User Lookup (input simulation)
            </button>
            <button onclick="switchTab('simulator')" id="tab-btn-simulator" class="pb-3 border-b-2 font-medium text-sm transition-all border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2">
                <i data-lucide="sliders" class="w-4 h-4"></i> Custom User Simulator
            </button>
        </div>

        <!-- Tab 1: Dashboard Table -->
        <div id="tab-dashboard" class="space-y-6">
            <div class="bg-white rounded-2xl shadow-sm border border-slate-200/80 overflow-hidden">
            <div class="p-6 border-b border-slate-100 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                    <div>
                        <h2 class="text-lg font-bold text-slate-900">E-Commerce Dataset Records</h2>
                        <p class="text-sm text-slate-500">Showing all 12 manual rows with calculated features and model predictions.</p>
                    </div>
                    <div class="flex items-center gap-3 w-full sm:w-auto">
                        <div class="relative w-full sm:w-64">
                            <i data-lucide="search" class="absolute left-3 top-2.5 w-4 h-4 text-slate-400"></i>
                            <input type="text" id="table-search" placeholder="Search user ID or product..." oninput="filterTable()" class="w-full pl-9 pr-4 py-2 text-sm bg-slate-50 border border-slate-200 rounded-xl focus:outline-none 
                            focus:ring-2 focus:ring-indigo-500">
                        </div>
                    </div>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-50 text-slate-400 font-semibold text-xs uppercase tracking-wider border-b border-slate-200">
                                <th class="py-3 px-6">User ID</th>
                                <th class="py-3 px-4">Product Type</th>
                                <th class="py-3 px-4">Device</th>
                                                                <th class="py-3 px-6">User ID</th>
                                <th class="py-3 px-4">Product Type</th>
                                <th class="py-3 px-4">Device</th>
                                <th class="py-3 px-4 text-center">Items Added</th>
                                <th class="py-3 px-4 text-center">Minutes Spent</th>
                                <th class="py-3 px-4 text-center">Discount</th>
                                <th class="py-3 px-4 text-center">Made Purchase</th>
                                <th class="py-3 px-4 text-center">Conv. Rate</th>
                                <th class="py-3 px-4 text-center">Prediction (Will Stay)</th>
                            </tr>
                        </thead>
                        <tbody id="user-table-body" class="divide-y divide-slate-100 text-sm">
                            <!-- Populated via JS -->
                        </tbody>
                    </table>
                         </div>
            </div>
        </div>

        <!-- Tab 2: User Lookup -->
        <div id="tab-lookup" class="hidden space-y-6">
            <div class="bg-white rounded-2xl shadow-sm border border-slate-200/80 p-6 sm:p-8 max-w-3xl mx-auto">
                <div class="text-center max-w-lg mx-auto mb-8">
                    <h2 class="text-xl font-bold text-slate-900">Target User Lookup</h2>
                    <p class="text-sm text-slate-500 mt-1">Select or type a User ID from the database to replicate the python `input("enter the 
                    user_id:")` lookup and see precise feature extraction.</p>
                </div>

                <div class="flex gap-3 max-w-md mx-auto mb-8">
                    <div class="relative flex-grow">
                        <i data-lucide="user" class="absolute left-3.5 top-3 w-5 h-5 text-slate-400"></i>
                        <input type="text" id="lookup-input" list="user-list" placeholder="e.g. USR101" class="w-full pl-11 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 font-medium">
                        <datalist id="user-list">
                         <option value="USR101"></option><option value="USR102"></option><option value="USR103"></option>
                            <option value="USR104"></option><option value="USR105"></option><option value="USR106"></option>
                            <option value="USR107"></option><option value="USR108"></option><option value="USR109"></option>
                            <option value="USR110"></option><option value="USR111"></option><option value="USR112"></option>
                        </datalist>
                    </div>
                    <button onclick="performLookup()" class="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-6 py-2.5 rounded-xl ransition-all shadow-sm flex items-center gap-2">
                        <i data-lucide="search" class="w-4 h-4"></i> Run Lookup
                    </button>
                </div>

                <!-- Lookup Result Card -->
                <div id="lookup-result-container" class="hidden space-y-6">
                    <div id="lookup-badge-banner" class="p-4 rounded-xl border flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div id="lookup-status-icon" class="p-2 rounded-lg"></div>
                            <div>
                                <h4 id="lookup-status-title" class="font-bold text-base"></h4>
                                 <p id="lookup-status-subtitle" class="text-xs"></p>
                            </div>
                        </div>
                        <span id="lookup-id-badge" class="px-3 py-1 font-mono font-bold rounded-lg text-sm"></span>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div class="bg-slate-50 p-4 rounded-xl border border-slate-200/60 space-y-3">
                            <h5 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Raw User Attributes</h5>
                            <div class="grid grid-cols-2 gap-2 text-sm">
                                <span class="text-slate-500">Product Type:</span><span id="res-product" class="font-medium text-slate-800"></span>
                                span><span id="res-product" class="font-medium text-slate-800"></span>
                                <span class="text-slate-500">Device Type:</span><span id="res-device" class="font-medium text-slate-800"></span>
                                <span class="text-slate-500">Items Added:</span><span id="res-items" class="font-medium text-slate-800"></span>
                                <span class="text-slate-500">Minutes Spent:</span><span id="res-mins" class="font-medium text-slate-800"></span>
                                <span class="text-slate-500">Used Discount:</span><span id="res-disc" class="font-medium 
                                text-slate-800"></span>
                                <span class="text-slate-500">Made Purchase:</span><span id="res-purch" class="font-medium text-slate-800"></span>
                            </div>
                        </div>

                        <div class="bg-slate-50 p-4 rounded-xl border border-slate-200/60 space-y-3">
                            <h5 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Extracted ML Features (X)</h5>
                            <div class="grid grid-cols-2 gap-2 text-sm">
                                <span class="text-slate-500">Conversion Rate:</
                                span><span id="res-conv" class="font-mono font-medium text-slate-800"></span>
                                <span class="text-slate-500">Items Abandoned:</span><span id="res-aband" class="font-mono font-medium text-slate-800"></span>
                                <span class="text-slate-500">Time Spent (mins):</span><span id="res-tspent" class="font-mono font-medium text-slate-800"></span>
                                <span class="text-slate-500">Discount Applied:</span><span id="res-dapplied" class="font-mono font-medium text-slate-800"></span>
                            </div>
                        </div>
                    </div>
                     <div class="bg-indigo-50/60 border border-indigo-100 p-4 rounded-xl flex items-start gap-3">
                        <i data-lucide="info" class="w-5 h-5 text-indigo-600 mt-0.5 shrink-0"></i>
                        <div class="text-xs text-indigo-900 leading-relaxed">
                            <strong class="font-semibold">Decision Rule Explanation:</strong> 
                                                        <strong class="font-semibold">Decision Rule Explanation:</strong> 
                                                         <!-- Tab 3: Custom User Simulator -->
        <div id="tab-simulator" class="hidden space-y-6">
            <div class="bg-white rounded-2xl shadow-sm border border-slate-200/80 p-6 sm:p-8 max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                <div class="space-y-6">
                    <div>
                        <h2 class="text-xl font-bold text-slate-900">Simulate Custom User</h2>
                        <p class="text-sm text-slate-500 mt-1">Adjust parameters below to test feature extraction and determine if the customer stays based on the decision rules.</p>
                    </div> <div class="space-y-4">
                        <div>
                            <div class="flex justify-between text-sm mb-1">
                                <label class="font-medium text-slate-700">Items Added</label>
                                <span id="val-items" class="font-bold text-indigo-600">3</span>
                            </div>
                            <input type="range" id="sim-items" min="0" max="20" value="3" oninput="updateSimulator()" class="w-full accent-indigo-600 cursor-pointer">
                        </div>

                        <div>
                            <div class="flex justify-between text-sm mb-1">
                                <label class="font-medium text-slate-700">Minutes Spent</label>
                                <span id="val-mins" class="font-bold text-indigo-600">15</span>
                            </div>
                            <input type="range" id="sim-mins" min="0" max="150" value="15" oninput="updateSimulator()" class="w-full accent-indigo-600 cursor-pointer">
                        </div>

                        <div>
                            <div class="flex justify-between text-sm mb-1">
                                <label class="font-medium text-slate-700">Made Purchase Count</label>
                                <span id="val-purch" class="font-bold text-indigo-600">1</span>
                            </div>
                            <input type="range" id="sim-purch" min="0" max="10" value="1" oninput="updateSimulator()" class="w-full accent-indigo-600 cursor-pointer">
                        </div>

                        <div class="grid grid-cols-2 gap-4">
                            <div><label class="block text-sm font-medium text-slate-700 mb-1">Used Discount</label>
                                <select id="sim-disc" onchange="updateSimulator()" class="w-full p-2.5 text-sm bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                    <option value="0">No (0)</option>
                                    <option value="1">Yes (1)</option>
                                    <option value="2">Multiple (2)</option>
                                    <option value="3">High (3)</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-slate-700 mb-1">Device Type</label>
                                <select id="sim-device" class="w-full p-2.5 text-sm bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                    <option value="Desktop">Desktop</option>
                                    <option value="Mobile">Mobile</option>
                                     </select>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Simulation Output Box -->
                <div class="bg-slate-50 p-6 sm:p-8 rounded-2xl border border-slate-200/80 flex flex-col items-center text-center justify-center space-y-6">
                    <div id="sim-status-icon-wrapper" class="p-4 rounded-2xl shadow-inner">
                        <i id="sim-icon" data-lucide="user-check" class="w-12 h-12"></i>
                    </div>
                    <div>
                        <span id="sim-badge" class="px-3 py-1 text-xs font-bold uppercase tracking-wider rounded-full"></span>
                        <h3 id="sim-title" class="text-2xl font-bold mt-2"></h3>
                          <p id="sim-desc" class="text-xs text-slate-500 mt-2 max-w-xs mx-auto"></p>
                    </div>

                    <div class="w-full border-t border-slate-200 pt-4 grid grid-cols-2 gap-4 text-left">
                        <div class="bg-white p-3 rounded-xl border border-slate-200/60">
                            <span class="text-xs text-slate-400 block">Conversion Rate</span>
                            <span id="sim-res-conv" class="text-sm font-mono font-bold text-slate-800">0.00</span>
                        </div>
                        <div class="bg-white p-3 rounded-xl border border-slate-200/60">
                            <span class="text-xs text-slate-400 block">Items Abandoned</span>
                             <span id="sim-res-aband" class="text-sm font-mono font-bold text-slate-800">0</span>
                            </div>
                    </div>
                </div>
            </div>
        </div>

    </main>

    
