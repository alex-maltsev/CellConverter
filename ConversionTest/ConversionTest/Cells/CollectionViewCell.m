//
//  CollectionViewCell.m
//  CellConversion
//
//  Created by Alexander Maltsev on 3/17/16.
//  Copyright © 2016 Alexander Maltsev. All rights reserved.
//

#import "CollectionViewCell.h"

@implementation CollectionViewCell

- (void)awakeFromNib
{
    // Initialization code
    self.myTextField.userInteractionEnabled = NO;
    
    self.myLabel.textColor = [UIColor darkGrayColor];
    [self.myButton setTintColor:[UIColor redColor]];
}


- (IBAction)myButtonPressed:(id)sender
{
    NSLog(@"myButton pressed in collection view cell");
}


- (IBAction)editingDidBegin:(id)sender
{
}

@end
