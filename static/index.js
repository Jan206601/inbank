const form = document.querySelector('#form');

const result_text_element = document.querySelector('#result-text');

form.addEventListener('submit', e => {
    e.preventDefault(); // prevent form submission

    const formData = new FormData(form);

    fetch('/api/check_loan', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        let decision = data['decision']
        if (decision !== undefined) {
            if (decision === null) {
                // Show error message if unable to calculate decision under given input conditions
                result_text_element.textContent = data['error_message'];
            } else {
                // Show decision
                let text = `<b>Decision: ${decision}</b><br>`;
                let min_period_for_amount = data['minimum_period_for_amount'];
                let max_amount_for_period = data['maximum_amount_for_period'];

                // Show maximum available amount for the desired period
                if (max_amount_for_period !== null) {
                    text += `Maximum amount for ${formData.get('period')} months: ${max_amount_for_period}€<br>`;
                } else {
                    text += `This period is not available for any amount.`;
                }
                if (decision === false) {
                    // If loan is not available for the desired period, suggest suitable period for the desired amount
                    if (min_period_for_amount !== null) {
                        text += `Minimum period for ${formData.get('amount')}€: ${min_period_for_amount} months`;
                    } else {
                        text += `This amount is not available for any period.`;
                    }
                }
                result_text_element.innerHTML = text;
            }
        }
    })
    .catch(error => {
        console.error(error);
    });

});
