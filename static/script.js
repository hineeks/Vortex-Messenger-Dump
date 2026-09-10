// File upload handling
const fileInput = document.getElementById('fileInput');
const uploadSection = document.getElementById('uploadSection');
const dashboardSection = document.getElementById('dashboardSection');

fileInput.addEventListener('change', handleFileUpload);

// Drag and drop
document.addEventListener('dragover', (e) => {
    e.preventDefault();
    document.querySelector('.upload-box').style.borderColor = '#764ba2';
});

document.addEventListener('dragleave', () => {
    document.querySelector('.upload-box').style.borderColor = '#667eea';
});

document.addEventListener('drop', (e) => {
    e.preventDefault();
    document.querySelector('.upload-box').style.borderColor = '#667eea';
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        handleFileUpload();
    }
});

function handleFileUpload() {
    const file = fileInput.files[0];
    if (!file) return;
    
    const formData = new FormData();
    formData.append('file', file);
    
    fetch('/api/upload', {
        method: 'POST',
        body: formData
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            uploadSection.style.display = 'none';
            dashboardSection.style.display = 'block';
            loadDashboard();
        } else {
            alert('Error: ' + data.error);
        }
    });
}

function loadDashboard() {
    // Load statistics
    fetch('/api/statistics')
    .then(r => r.json())
    .then(stats => {
        document.getElementById('totalMessages').textContent = stats.total_messages.toLocaleString();
        document.getElementById('uniqueUsers').textContent = stats.unique_users;
        document.getElementById('avgMessages').textContent = stats.average_messages_per_user.toFixed(2);
    });
    
    // Load activity
    fetch('/api/activity')
    .then(r => r.json())
    .then(activity => {
        document.getElementById('peakHour').textContent = (activity.peak_hour || '--') + ':00';
    });
}

function searchMessages() {
    const query = document.getElementById('searchQuery').value;
    if (!query) return;
    
    const resultsDiv = document.getElementById('searchResults');
    resultsDiv.innerHTML = '<div class="loading"></div> Поиск...';
    
    fetch('/api/search', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({query: query})
    })
    .then(r => r.json())
    .then(data => {
        if (data.results.length === 0) {
            resultsDiv.innerHTML = '<p style="color: #999; padding: 20px; text-align: center;">Ничего не найдено</p>';
            return;
        }
        
        resultsDiv.innerHTML = data.results.map(msg => `
            <div class="result-item">
                <div class="result-timestamp">${msg.timestamp}</div>
                <div class="result-user">${msg.username || 'Unknown'}</div>
                <div class="result-content">${msg.content}</div>
            </div>
        `).join('');
    });
}

function exportData() {
    const format = document.getElementById('exportFormat').value;
    fetch('/api/export', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({format: format})
    })
    .then(r => r.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `export.${format}`;
        a.click();
        window.URL.revokeObjectURL(url);
    })
    .catch(e => alert('Export failed: ' + e.message));
}
