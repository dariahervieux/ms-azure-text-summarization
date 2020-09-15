import { Injectable } from '@angular/core';
import { HttpClient, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadService {

  constructor(private httpClient: HttpClient) { }

  public upload(url: string, formData: FormData): Observable<HttpEvent<string>> {

    return this.httpClient.post<string>(url, formData, {  
        reportProgress: true,  
        observe: 'events'  
      });  
  }
  
}
