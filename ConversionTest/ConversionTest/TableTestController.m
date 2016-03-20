//
//  TableTestController.m
//  ConversionTest
//
//  Created by Alexander Maltsev on 3/19/16.
//  Copyright © 2016 self. All rights reserved.
//

#import "TableTestController.h"

#define TABLE_CELL_XIB_NAME @"TableViewCell"
#define TABLE_CELL_HEIGHT 50.0

@interface TableTestController () <UITableViewDataSource, UITableViewDelegate>

@property (weak, nonatomic) IBOutlet UITableView *tableView;

@end

@implementation TableTestController

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    [self.tableView registerNib:[UINib nibWithNibName:TABLE_CELL_XIB_NAME bundle:nil] forCellReuseIdentifier:TABLE_CELL_XIB_NAME];
}


- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return 5;
}


- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *cell = [self.tableView dequeueReusableCellWithIdentifier:TABLE_CELL_XIB_NAME forIndexPath:indexPath];
    return cell;
}


- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    return TABLE_CELL_HEIGHT;
}

@end
