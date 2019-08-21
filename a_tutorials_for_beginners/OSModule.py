import os

#print(dir(os))

#os.access(path, mode)
#os.F_OK  — Found
#os.R_OK  — Readable
#os.W_OK  — Writable
#os.X_OK  — Executable

print(os.access('./CopyFile.py', os.R_OK))
#os.chdir('C:\\Users\\lifei\\Desktop')
#chflags(path,flags)
 #os.UF_NODUMP – Don’t dump the file
 #os.UF_IMMUTABLE − You may not change the file
 #os.UF_APPEND − You may only append to the file
# os.UF_NOUNLINK – You may not rename or delete the file
# os.UF_OPAQUE − The directory is opaque when we view it through a union stack
 #os.SF_ARCHIVED – You may archive the file
# os.SF_IMMUTABLE – You may not change the file
# os.SF_APPEND – You may only append to the file
 #os.SF_NOUNLINK – You may not rename or delete the file
# os.SF_SNAPSHOT − It is a snapshot file


os.chmod()

stat.S_ISUID − Set user ID on execution
stat.S_ISGID − Set group ID on execution
stat.S_ENFMT – Enforced record locking
stat.S_ISVTX – After execution, save text image
stat.S_IREAD − Read by owner
stat.S_IWRITE − Write by owner
stat.S_IEXEC − Execute by owner
stat.S_IRWXU − Read, write, and execute by owner
stat.S_IRUSR − Read by owner
stat.S_IWUSR − Write by owner
stat.S_IXUSR − Execute by owner
stat.S_IRWXG − Read, write, and execute by group
stat.S_IRGRP − Read by group
stat.S_IWGRP − Write by group
stat.S_IXGRP − Execute by group
stat.S_IRWXO − Read, write, and execute by others
stat.S_IROTH − Read by others
stat.S_IWOTH − Write by others
stat.S_IXOTH − Execute by others


chown(path,uid,gid)
os.chown("Today.txt", 100, -1)


os.close() closes the associated file with descriptor fd.
fd=os.open('Today.txt',os.O_RDWR)
os.close(fd)
closerange(fd_low,fd_high)