import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { FileDragDropDirective } from './file-drag-drop.directive';
import { OneFileUploadComponent } from './one-file-upload/one-file-upload.component';

@NgModule({
  imports: [
    CommonModule,
    MatButtonModule
  ],
  declarations: [FileDragDropDirective, OneFileUploadComponent],
  exports: [OneFileUploadComponent]
})
export class FileUploadModule { }