// Simple API functions to interact with the backend
const studentAPI = {
  // Get all students
  getAll: async function() {
    try {
      const response = await fetch('/api/students');
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    } catch (error) {
      console.error("Error fetching students:", error);
      return {};
    }
  },

  // Add a new student
  add: async function(name) {
    try {
      const response = await fetch('/api/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
      });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    } catch (error) {
      console.error("Error creating student:", error);
      throw error;
    }
  },

  // Update a student's name
  update: async function(oldName, newName) {
    try {
      const response = await fetch(`/api/students/${encodeURIComponent(oldName)}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ new_name: newName })
      });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    } catch (error) {
      console.error("Error updating student:", error);
      throw error;
    }
  },

  // Delete a student
  delete: async function(name) {
    try {
      const response = await fetch(`/api/students/${encodeURIComponent(name)}`, {
        method: 'DELETE'
      });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    } catch (error) {
      console.error("Error deleting student:", error);
      throw error;
    }
  }
};

// When the page loads
document.addEventListener('DOMContentLoaded', function() {
  // Get references to important elements
  const tableContainer = document.getElementById('showTable');
  const addForm = document.getElementById('addStudentForm');
  const nameInput = document.getElementById('studentNameInput');
  const addButton = document.getElementById('submitStudentButton');
  const statusMessage = document.getElementById('statusMessage');

  // Function to show messages to the user
  function showMessage(message, isError = false) {
    statusMessage.textContent = message;
    statusMessage.className = isError ? 'error-message' : 'success-message';
  }

  // Function to create the students table
  function createStudentsTable(students) {
    // Clear the container
    tableContainer.innerHTML = '';

    // Check if we have any students
    if (Object.keys(students).length === 0) {
      tableContainer.innerHTML = '<p>Nu există studenți. Adăugați un student nou folosind formularul de mai jos.</p>';
      return;
    }

    // Create the table
    const table = document.createElement('table');

    // Add table header
    const header = document.createElement('tr');
    ['Nume', 'Schimbă Nume', 'Salvează', 'Șterge'].forEach(text => {
      const th = document.createElement('th');
      th.textContent = text;
      header.appendChild(th);
    });
    table.appendChild(header);

    // Add a row for each student
    Object.keys(students).forEach(name => {
      const row = document.createElement('tr');

      // Name cell
      const nameCell = document.createElement('td');
      nameCell.textContent = name;
      row.appendChild(nameCell);

      // New name input cell
      const inputCell = document.createElement('td');
      const input = document.createElement('input');
      input.type = 'text';
      input.placeholder = 'Nume nou';
      inputCell.appendChild(input);
      row.appendChild(inputCell);

      // Save button cell
      const saveCell = document.createElement('td');
      const saveButton = document.createElement('button');
      saveButton.textContent = 'Salvează';
      saveButton.onclick = async () => {
        const newName = input.value.trim();
        if (newName && newName !== name) {
          try {
            await studentAPI.update(name, newName);
            showMessage(`Nume schimbat din '${name}' în '${newName}'`);
            loadStudents(); // Refresh the table
          } catch (error) {
            showMessage(`Eroare: ${error.message}`, true);
          }
        }
      };
      saveCell.appendChild(saveButton);
      row.appendChild(saveCell);

      // Delete button cell
      const deleteCell = document.createElement('td');
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Șterge';
      deleteButton.onclick = async () => {
        try {
          await studentAPI.delete(name);
          showMessage(`Student '${name}' șters`);
          loadStudents(); // Refresh the table
        } catch (error) {
          showMessage(`Eroare: ${error.message}`, true);
        }
      };
      deleteCell.appendChild(deleteButton);
      row.appendChild(deleteCell);

      table.appendChild(row);
    });

    tableContainer.appendChild(table);
  }

  // Function to load and display all students
  async function loadStudents() {
    try {
      const students = await studentAPI.getAll();
      createStudentsTable(students);
    } catch (error) {
      showMessage(`Eroare la încărcarea studenților: ${error.message}`, true);
    }
  }

  // Load students when the page loads
  loadStudents();

  // Set up the add student form
  addForm.onsubmit = async function(event) {
    event.preventDefault();
    const name = nameInput.value.trim();

    if (name) {
      try {
        await studentAPI.add(name);
        showMessage(`Student '${name}' adăugat`);
        nameInput.value = ''; // Clear the input
        loadStudents(); // Refresh the table
      } catch (error) {
        showMessage(`Eroare: ${error.message}`, true);
      }
    }
  };
});