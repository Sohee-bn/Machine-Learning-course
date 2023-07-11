

function spilan()
clc
clear
close all
%reading features and labels from file
x=load('features.txt');
y=load('labels.txt');
%70% of data  is considered as train set 
x_train=x(1:70);%train data for feature
y_train=y(1:70);%train data for label
 

landa=0.5;
q=[0 4 9];%q=3
k=7;
d=eye(k,k);% Identity matrix
phi=zeros(70,7);% 7 is degre


%spline:


for i=1:70
    if x(i)>q(1);
        k1=x(i)-q(1);
    else
        k1=0;
    end%ended part one
    if x(i)>q(2);
        k2=x(i)-q(2);
    else 
        k2=0;
    end% ended part two
         if x(i)>q(3);
        k3=x(i)-q(3);
    else
        k3=0;
         end%ended part three
    phi(i,:)=[1 x(i) x(i)^2 x(i)^3 k1^3 k2^3 k3^3]; % y=a+bx => calculating the formula for phi
end
w=inv(phi'*phi-landa*d)*phi'*y_train; %calculating the formula for w


% calculating the formula phi for test

x_test=x(71:100);
phi1=zeros(30,7);
for i=1:30
    if x_test(i)>q(1);
        k1=x_test(i)-q(1);
    else
        k1=0;
    end
    if x_test(i)>q(2);
        k2=x_test(i)-q(2);
    else
        k2=0;
    end
         if x_test(i)>q(3);
        k3=x_test(i)-q(3);
    else
        k3=0;
         end

    phi1(i,:)=[1 x_test(i) x_test(i)^2 x_test(i)^3 k1^3 k2^3 k3^3];%%calculating the formula for phi of test data
end
    h_test=phi1*w;% a function for fitting
     subplot(211);
    plot(x_train,y_train,'*','color','red');
    subplot(212);
    plot(x_test,h_test,'*','color','m');%drow our test_x and h_x
    hold on;
    %represention for joined test data
 count=1;
for i=-6:0.1:12
    if i>q(1);
        k1=i-q(1);
    else
        k1=0;
    end
    if i>q(2);
        k2=i-q(2);
    else
        k2=0;
    end
         if i>q(3);
        k3=i-q(3);
    else
        k3=0;
         end
    yy(count)=[1 i i^2 i^3 k1^3 k2^3 k3^3]*w;
    count=count+1;
end
plot([-6:0.1:12],yy)
