import { HttpClient } from '@angular/common/http';
import { Component, inject } from '@angular/core';
import { ReactiveFormsModule, FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-cars',
  imports: [ReactiveFormsModule],
  templateUrl: './cars.component.html',
  styleUrl: './cars.component.css',
})
export class CarsComponent {
  http = inject(HttpClient);
  cars: any = [];

  // Backend to save orders
  private orderApiUrl = 'http://localhost:5050/order';

  carsFilter = [
    { active: true, name: 'All cars' },
    { active: false, name: 'Lamborghini' },
    { active: false, name: 'Ferrari' },
    { active: false, name: 'Porsche' },
    { active: false, name: 'BMW' },
    { active: false, name: 'Mercedes' },
    { active: false, name: 'Chevrolet' },
    { active: false, name: 'Audi' },
    { active: false, name: 'Ford' },
  ];

  orderForm = new FormGroup({
    car: new FormControl(''),
    name: new FormControl(''),
    phone: new FormControl(''),
  });

  ngOnInit() {
    this.getCars('');
  }

  getCars(filter: string) {
  this.http.get<any[]>('/data/cars.json').subscribe({
    next: (data) => {
      if (filter && filter !== 'All cars') {
        this.cars = data.filter(car =>
          car.title.toLowerCase().includes(filter.toLowerCase())
        );
      } else {
        this.cars = data;
      }
    },
    error: (err) => console.error('Error loading cars:', err),
  });
}

  changeFilter(filter: any, carsContent: HTMLElement) {
    this.carsFilter.forEach((el) => (el.active = false));
    filter.active = true;

    this.getCars(filter.name);

    carsContent.scrollIntoView({ behavior: 'instant' });
  }

  isError(fieldName: string) {
    const control = this.orderForm.get(fieldName);
    return !!(control?.invalid && (control?.dirty || control?.touched));
  }

  sendOrder() {
    if (this.orderForm.valid) {
      this.http
        .post(this.orderApiUrl, this.orderForm.value)
        .subscribe({
          next: (response: any) => {
            alert(response.message || 'Your order has been submitted successfully');
            this.orderForm.reset();
          },
          error: (response: any) => {
            alert(response.error?.message || 'Error submitting your order');
          },
        });
    } else {
      alert('Please fill out the form correctly before submitting.');
    }
  }
}
