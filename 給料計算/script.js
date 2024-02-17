document.getElementById('salaryForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const baseSalary = parseFloat(document.getElementById('baseSalary').value);
    const NightbaseSalary = parseFloat(document.getElementById('NightbaseSalary').value);
    const hoursWorked = parseFloat(document.getElementById('hoursWorked').value);
    const NighthoursWorked = parseFloat(document.getElementById('NighthoursWorked').value);
    const dailyAllowance = parseFloat(document.getElementById('dailyAllowance').value);
    const daysWorked = parseFloat(document.getElementById('daysWorked').value);
    const transportationAllowance = parseFloat(document.getElementById('transportationAllowance').value);

    const totalSalary = (baseSalary * hoursWorked) + (NightbaseSalary * NighthoursWorked) + (dailyAllowance * daysWorked) + (transportationAllowance * daysWorked);

    document.getElementById('result').innerText = `給与: ${totalSalary} 円`;
    document.getElementById('result').style.display = 'block';
});
