function unt()

%clear all;
close all;
set(gcf,'color','w')

colors = {'red','blue','green','black','magenta','cyan', ...
    [0.4 0.7 0.1],[0.7 0.4 0.1],[0.1 0.4 0.7],[0.7, 0.7, 0]};
legend_names = {'Number of filters','Batch size','Momentum','Learning rate'};
max_values = [100.0,double(2^8),1.0,10^-0.5]

xlabeltext = 'Value/MaxValue';
ylabeltext = 'Validation error (%)';

irun=1;
filename = ['solutions_5_' num2str(irun) '.txt'];
M = dlmread(filename);  % epoch_index   total_time  train_loss  val_loss    val_error

leg ={};
ii = 1;
for i=[1,2,3,4]
    xvals=M(:,i);
    xvals=xvals./max_values(i);
    yvals=100.0-M(:,5);
    leg(ii) = legend_names(i);
    ii = ii + 1;

    scatter(xvals, yvals); hold on;
end;

set(gca,'yscale','log')
legend(leg,'Location','SouthWest');
xlabel(xlabeltext,'fontsize',16);
ylabel(ylabeltext,'fontsize',16); 