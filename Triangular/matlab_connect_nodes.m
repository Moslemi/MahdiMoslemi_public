clear all
%table des coordonnées
% lecture du fichier coordonnées geométriques
vcor= importdata('maillage1.txt');
% table des connecrivités
% lecture du fichier des connectivités
kconec=importdata('connectivite1.txt');
% définition du nomdre de noeuds et d'éléments
nnt=size(vcor,1);      % nombre de noeuds
nelt=size(kconec,1);   % nombre d'éléments
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