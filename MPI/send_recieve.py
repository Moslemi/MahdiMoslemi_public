# mpi.run.openmpi -np 2 -machine file "directory" python "name of the file"

from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

shared = (rank+1)*5

if rank == 1:
    data = shared
    comm.send(data,dest =0)
    print('from rank',rank,'we sent',data)

elif rank ==0:
    data = comm.recv(source=1)
    print('on node',rank,'we received:',data)

