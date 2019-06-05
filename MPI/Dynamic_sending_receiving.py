from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

shared = (rank+1)* 7

comm.send(shared,dest=(rank+1) %size)
data = comm.recv(source=(rank-1)%size)

print(name)
print('Rank:',rank)
print("Received:",data,'which came from rank:',(rank-1)%size)