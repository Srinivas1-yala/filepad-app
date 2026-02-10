from django.db import models
import os


def user_directory_path(instance, filename):
    """Generate upload path based on user's password hash"""
    # CRITICAL FIX: Use instance.user_space.user_hash (not instance.user_hash)
    return os.path.join('filepad', instance.user_space.user_hash, filename)


class UserSpace(models.Model):
    """Model to store user spaces based on password hash"""
    user_hash = models.CharField(max_length=64, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_accessed']

    def __str__(self):
        return f"UserSpace: {self.user_hash[:10]}..."


class UploadedFile(models.Model):
    """Model to store uploaded files"""
    user_space = models.ForeignKey(UserSpace, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=user_directory_path)
    original_filename = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    file_type = models.CharField(max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.original_filename} - {self.user_space.user_hash[:10]}..."

    def delete(self, *args, **kwargs):
        """Override delete to remove file from storage"""
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)

    @property
    def file_url(self):
        """Get the URL of the file"""
        if self.file:
            return self.file.url
        return None
