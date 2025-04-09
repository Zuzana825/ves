
document.addEventListener('DOMContentLoaded', function() {
	const shapeFields = {
	  'CLEAR': [
		{ name: 'color', label: 'Farba (hex):', type: 'color', default: '#ff0000' }
	  ],
	  'FILL_TRIANGLE': [
		{ name: 'x1', label: 'X1:', type: 'number', placeholder: '200' },
		{ name: 'y1', label: 'Y1:', type: 'number', placeholder: '100' },
		{ name: 'x2', label: 'X2:', type: 'number', placeholder: '400' },
		{ name: 'y2', label: 'Y2:', type: 'number', placeholder: '300' },
		{ name: 'x3', label: 'X3:', type: 'number', placeholder: '300' },
		{ name: 'y3', label: 'Y3:', type: 'number', placeholder: '300' },
		{ name: 'color', label: 'Farba výplne:', type: 'color', default: '#0000ff' }
	  ],
	  'FILL_CIRCLE': [
		{ name: 'cx', label: 'Stred X:', type: 'number', placeholder: '200' },
		{ name: 'cy', label: 'Stred Y:', type: 'number', placeholder: '100' },
		{ name: 'radius', label: 'Polomer:', type: 'number', placeholder: '50' },
		{ name: 'color', label: 'Farba výplne:', type: 'color', default: '#00ff00' }
	  ],
	  'FILL_RECT': [
		{ name: 'x', label: 'Horná ľavá X:', type: 'number', placeholder: '400' },
		{ name: 'y', label: 'Horná ľavá Y:', type: 'number', placeholder: '100' },
		{ name: 'width', label: 'Šírka:', type: 'number', placeholder: '150' },
		{ name: 'height', label: 'Výška:', type: 'number', placeholder: '200' },
		{ name: 'color', label: 'Farba výplne:', type: 'color', default: '#00ff00' }
	  ],
	  'CIRCLE': [
		{ name: 'cx', label: 'Stred X:', type: 'number', placeholder: '300' },
		{ name: 'cy', label: 'Stred Y:', type: 'number', placeholder: '200' },
		{ name: 'radius', label: 'Polomer:', type: 'number', placeholder: '100' },
		{ name: 'thickness', label: 'Hrúbka:', type: 'number', placeholder: '1', default: '1' },
		{ name: 'color', label: 'Farba:', type: 'color', default: '#ffffff' }
	  ],
	  'TRIANGLE': [
		{ name: 'x1', label: 'X1:', type: 'number', placeholder: '50' },
		{ name: 'y1', label: 'Y1:', type: 'number', placeholder: '100' },
		{ name: 'x2', label: 'X2:', type: 'number', placeholder: '200' },
		{ name: 'y2', label: 'Y2:', type: 'number', placeholder: '300' },
		{ name: 'x3', label: 'X3:', type: 'number', placeholder: '150' },
		{ name: 'y3', label: 'Y3:', type: 'number', placeholder: '200' },
		{ name: 'thickness', label: 'Hrúbka:', type: 'number', placeholder: '1', default: '1' },
		{ name: 'color', label: 'Farba:', type: 'color', default: '#00ff00' }
	  ],
	  'RECT': [
		{ name: 'x', label: 'Horná ľavá X:', type: 'number', placeholder: '200' },
		{ name: 'y', label: 'Horná ľavá Y:', type: 'number', placeholder: '100' },
		{ name: 'width', label: 'Šírka:', type: 'number', placeholder: '300' },
		{ name: 'height', label: 'Výška:', type: 'number', placeholder: '100' },
		{ name: 'thickness', label: 'Hrúbka:', type: 'number', placeholder: '1', default: '1' },
		{ name: 'color', label: 'Farba:', type: 'color', default: '#000000' }
	  ],
	  'LINE': [
		{ name: 'x1', label: 'X1:', type: 'number', placeholder: '0' },
		{ name: 'y1', label: 'Y1:', type: 'number', placeholder: '0' },
		{ name: 'x2', label: 'X2:', type: 'number', placeholder: '599' },
		{ name: 'y2', label: 'Y2:', type: 'number', placeholder: '399' },
		{ name: 'thickness', label: 'Hrúbka:', type: 'number', placeholder: '1', default: '1' },
		{ name: 'color', label: 'Farba:', type: 'color', default: '#000000' }
	  ]
	};
  
	const shapeSelect = document.getElementById('shapeSelect');
	const shapeInputsDiv = document.getElementById('shapeInputs');
	const addShapeBtn = document.getElementById('addShapeButton');
	const vesTextarea = document.querySelector("textarea[name='ves']");
  
	function updateShapeInputs() {
	  const shape = shapeSelect.value;
	  const fields = shapeFields[shape];
	  let html = "";
	  fields.forEach(field => {
		html += `<label for="${field.name}">${field.label}</label>`;
		html += `<input type="${field.type}" id="${field.name}" `;
		if (field.placeholder) html += `placeholder="${field.placeholder}" `;
		if (field.default) html += `value="${field.default}" `;
		html += `/>`;
	  });
	  shapeInputsDiv.innerHTML = html;
	}
	updateShapeInputs();
	shapeSelect.addEventListener("change", updateShapeInputs);
  
	addShapeBtn.addEventListener("click", function(){
	  const shape = shapeSelect.value;
	  const fields = shapeFields[shape];
	  let command = shape;
	  fields.forEach(field => {
		const value = document.getElementById(field.name).value.trim();
		command += " " + value;
	  });
	  if (vesTextarea.value.trim() !== "") {
		vesTextarea.value += "\n" + command;
	  } else {
		vesTextarea.value = command;
	  }
	});
  
	function handleSubmit(e) {
	  e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači
	  // this reprezentuje ten formulár, ktorý odosielame
	  const ves = this.querySelector("textarea").value; // Načítame text z textarea
	  const width = document.querySelector("section:nth-child(2)").clientWidth; // Načítame aktuálnu šírku výstupného okna
	  const formular = new URLSearchParams(); // Vytvoríme štruktúru, ktorá bude reprezentovať formulár
	  formular.append('ves', ves); // Pridáme tam naše hodnoty
	  formular.append('width', width);
	  const url = this.action; // Načítame pôvodnú URL z formulára
	  const method = this.method; // Načítame pôvodnú metódu z formulára
	  fetch(url, { method: method, body: formular })
		.then((res) => res.blob())
		.then((image) => {
		  document.querySelector("#output").src = URL.createObjectURL(image);
		});
	}
	document.querySelector("form").addEventListener("submit", handleSubmit);
  });
  