package store.product;

import java.math.BigDecimal;
import jakarta.validation.constraints.*;
import lombok.Builder;
import lombok.experimental.Accessors;

@Builder @Accessors(fluent = true)
public record ProductIn(
    String name,
    Double price,
    String unit
) {
    
}
