clear all
%table des coordonn�es
% lecture du fichier coordonn�es geom�triques
vcor= importdata('maillage1.txt');
% table des connecrivit�s
% lecture du fichier des connectivit�s
kconec=importdata('connectivite1.txt');
% d�finition du nomdre de noeuds et d'�l�ments
nnt=size(vcor,1);      % nombre de noeuds
nelt=size(kconec,1);   % nombre d'�l�ments
ndln=1;                % nombre de ddl par noeud
ndlt=nnt*ndln;         % nombre de ddl total
% affichage du maillage
for ie=1:nelt
    % ie
    % kconec(ie,:)
    % kconec(ie,1)
    x=vcor([kconec(ie,:),kconec(ie,1)],1)';
    y=vcor([kconec(ie,:),kconec(ie,1)],2)';
%    pause
%   pause
   plot(x,y,'o-')
   hold on
end