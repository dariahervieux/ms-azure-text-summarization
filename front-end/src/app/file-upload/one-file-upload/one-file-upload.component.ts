import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-one-file-upload',
  templateUrl: './one-file-upload.component.html',
  styleUrls: ['./one-file-upload.component.scss']
})
export class OneFileUploadComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  /**
   * on file drop handler
   */
  onFileDropped($event) {
    
  }

  /**
   * handle file from browsing
   */
  fileBrowseHandler(files) {
    
  }

}