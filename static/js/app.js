const url = 'http://localhost:8181';

// Handle form submission for adding a new contact
document.getElementById('add_new_contact_form').addEventListener('submit', (event) => {
    event.preventDefault();

    const full_name = document.getElementById('full_name').value;
    const mobile_number = document.getElementById('mobile_number').value;
    const email_id = document.getElementById('email_id').value;

    const uri = `${url}/add-contact`;
    const data = {
        full_name,
        mobile_number,
        email_id
    };

    fetch(uri, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert(JSON.stringify(data, null, 4));
            document.getElementById('add_new_contact_form').reset();
            window.location.href = '/';
        })
        .catch(error => {
            console.error(error);
            alert(JSON.stringify(error, null, 4));
        });
});

// Search function to filter contact list
function search_function() {
    const input = document.getElementById("search_contact");
    const filter = input.value.toUpperCase();
    const table = document.getElementById("contact-list");
    const tr = table.getElementsByTagName("tr");

    for (let i = 0; i < tr.length; i++) {
        const td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            const txtValue = td.textContent || td.innerText;
            tr[i].style.display = txtValue.toUpperCase().includes(filter) ? "" : "none";
        }
    }
}

// Delete a contact by id
function delete_contact(contact_id) {
    const uri = `${url}/delete-contact/${contact_id}`;
    fetch(uri, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert(JSON.stringify(data, null, 4));
            window.location.href = '/';
        })
        .catch(error => {
            console.error(error);
            alert(JSON.stringify(error, null, 4));
        });
}

// Get contact details by id and show update modal
function update_contact(contact_id) {
    document.getElementById('update_contact_modal').style.display = 'block';
    const uri = `${url}/get-contact/${contact_id}`;

    fetch(uri)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById('contact__id').value = data.id;
            document.getElementById('full__name').value = data.full_name;
            document.getElementById('mobile__number').value = data.mobile_number;
            document.getElementById('email__id').value = data.email_id;
        })
        .catch(error => {
            console.error(error);
            alert(JSON.stringify(error, null, 4));
        });
}

// Handle form submission for updating a contact
document.getElementById('update_contact_form').addEventListener('submit', (event) => {
    event.preventDefault();

    const contact__id = document.getElementById('contact__id').value;
    const full__name = document.getElementById('full__name').value;
    const mobile__number = document.getElementById('mobile__number').value;
    const email__id = document.getElementById('email__id').value;

    const uri = `${url}/update-contact/${contact__id}`;
    const data = {
        full_name: full__name,
        mobile_number: mobile__number,
        email_id: email__id
    };

    fetch(uri, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert(JSON.stringify(data, null, 4));
            document.getElementById('update_contact_form').reset();
            window.location.href = '/';
        })
        .catch(error => {
            console.error(error);
            alert(JSON.stringify(error, null, 4));
        });
});