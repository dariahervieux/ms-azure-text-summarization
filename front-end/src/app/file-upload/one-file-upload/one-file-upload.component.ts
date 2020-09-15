import { Component, OnInit } from '@angular/core';
import { UploadService } from '../upload.service';
import { of } from 'rxjs';  
import { catchError, map } from 'rxjs/operators'; 
import { HttpEventType, HttpErrorResponse } from '@angular/common/http';


@Component({
  selector: 'app-one-file-upload',
  templateUrl: './one-file-upload.component.html',
  styleUrls: ['./one-file-upload.component.scss']
})
export class OneFileUploadComponent implements OnInit {
  private fileInProgress: FileInProgress; 

  constructor(private uploadService: UploadService) { }

  ngOnInit() {
  }

  /**
   * handle file from browsing
   */
  fileBrowseHandler(files : FileList) {
    const formData = new FormData();  
    const file = files[0];
    this.fileInProgress = {file: file, inProgress: false, progressPrct: 0};
    formData.append('file', file);  
    this.fileInProgress.inProgress = true;  
    this.uploadService.upload('/start',formData).pipe(
      //TODO: use touch 
      map(event => {  
        switch (event.type) {  
          case HttpEventType.UploadProgress:  
          this.fileInProgress.progressPrct = Math.round(event.loaded * 100 / event.total);  
            break;  
          case HttpEventType.Response:  
            return event;  
        }  
      }),  
      catchError((error: HttpErrorResponse) => {  
        this.fileInProgress.inProgress = false;  
        return of(`${this.fileInProgress.file.name} upload failed.`);  
      })).subscribe((event: any) => {  
        if (typeof (event) === 'object') {  
          console.log(event.body);  
        }  
      });  
  }

}

interface FileInProgress {
  file: File,
  inProgress: boolean,
  progressPrct: number
}