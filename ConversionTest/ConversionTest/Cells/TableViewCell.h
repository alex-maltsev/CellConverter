//
//  TableViewCell.h
//  CellConversion
//
//  Created by Alexander Maltsev on 3/17/16.
//  Copyright © 2016 Alexander Maltsev. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface TableViewCell : UITableViewCell

@property (weak, nonatomic) IBOutlet UILabel *myLabel;
@property (weak, nonatomic) IBOutlet UIButton *myButton;
@property (weak, nonatomic) IBOutlet UITextField *myTextField;

@end
